"""
Book Club database — ranked-choice ballots + waiting-room cards.

Self-contained. Uses SQLite locally, picks up DATABASE_URL if set (Railway
can mount a volume at /app/data or provision Postgres later).
"""

from __future__ import annotations

import json as _json
import logging
import os
from datetime import datetime
from typing import Dict, List, Optional

from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

logger = logging.getLogger("book-club.db")

# Default to data/book_club.db on a Railway volume mount or locally under ./data
DEFAULT_DB_PATH = os.getenv("BOOK_CLUB_DB_PATH") or os.path.join(
    os.getenv("RAILWAY_VOLUME_MOUNT_PATH", "./data"), "book_club.db"
)
os.makedirs(os.path.dirname(DEFAULT_DB_PATH), exist_ok=True)

DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DEFAULT_DB_PATH}")

# SQLAlchemy needs check_same_thread=False for SQLite under FastAPI's async routes
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class BookVote(Base):
    __tablename__ = "book_votes"

    id = Column(Integer, primary_key=True)
    voter_name = Column(String, nullable=False, unique=True, index=True)
    vote_data = Column(Text, nullable=False)  # JSON: {rank1, rank2, rank3, rank4, veto}
    ip_address = Column(String, nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class VoteCard(Base):
    """User-submitted cards shown while waiting for all votes."""

    __tablename__ = "vote_cards"

    id = Column(Integer, primary_key=True)
    author = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Book(Base):
    """Ballot candidates. status: 'active' (votable), 'suggested' (awaiting
    admin approval), 'archived' (retired when a round is reset)."""

    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    pages = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    url = Column(String, nullable=True)
    status = Column(String, nullable=False, default="active", index=True)
    suggested_by = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class VoteRound(Base):
    """Frozen snapshot of a completed voting round, written on admin reset.

    snapshot JSON: {label, books, ballots, results, cards, winner}
    winner/total_ballots duplicated as columns for cheap history listings."""

    __tablename__ = "vote_rounds"

    id = Column(Integer, primary_key=True)
    label = Column(String, nullable=True)
    winner = Column(String, nullable=True)
    total_ballots = Column(Integer, nullable=False, default=0)
    snapshot = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


def init_db() -> None:
    """Create tables on startup. Idempotent."""
    Base.metadata.create_all(bind=engine)


# ---------------------------------------------------------------------------
# Helpers — copied from Life's backend/database.py, unchanged behavior.


def upsert_book_vote(voter_name: str, vote_data: dict, ip_address: str = None) -> Dict:
    """Insert or update a vote, matching by first name (case-insensitive)."""
    db = SessionLocal()
    try:
        first_name = voter_name.strip().split()[0].lower()
        rows = db.query(BookVote).all()
        row = None
        for r in rows:
            if r.voter_name.strip().split()[0].lower() == first_name:
                row = r
                break

        updated = row is not None
        if row:
            row.voter_name = voter_name
            row.vote_data = _json.dumps(vote_data)
            row.updated_at = datetime.utcnow()
        else:
            db.add(BookVote(voter_name=voter_name, vote_data=_json.dumps(vote_data)))
        db.commit()
        return {"success": True, "updated": updated}
    except Exception as e:
        logger.error(f"Error upserting book vote: {e}")
        db.rollback()
        return {"success": False, "reason": "error"}
    finally:
        db.close()


def get_vote_results() -> Dict:
    """Ranked choice voting (instant runoff) with veto elimination."""
    db = SessionLocal()
    try:
        rows = db.query(BookVote).all()
        ballots = []
        vetoed = set()
        for row in rows:
            try:
                ballot = _json.loads(row.vote_data)
            except Exception:
                continue
            prefs = [ballot.get("rank1"), ballot.get("rank2"), ballot.get("rank3"), ballot.get("rank4")]
            prefs = [b for b in prefs if b]
            ballots.append(prefs)
            v = ballot.get("veto")
            if v:
                vetoed.add(v)

        if vetoed:
            ballots = [[b for b in prefs if b not in vetoed] for prefs in ballots]

        candidates = set()
        for prefs in ballots:
            candidates.update(prefs)

        all_first_choices: Dict[str, int] = {c: 0 for c in candidates}
        for prefs in ballots:
            for b in prefs:
                if b in candidates:
                    all_first_choices[b] += 1
                    break
        zero_vote_books = {b for b, c in all_first_choices.items() if c == 0}
        candidates -= zero_vote_books
        eliminated_order = list(sorted(zero_vote_books))
        ranking: List[str] = []

        rounds = []

        def _nth_place_counts(books, rank_pos):
            pc = {b: 0 for b in books}
            for prefs in ballots:
                if rank_pos < len(prefs) and prefs[rank_pos] in pc:
                    pc[prefs[rank_pos]] += 1
            return pc

        while candidates:
            counts: Dict[str, int] = {c: 0 for c in candidates}
            active_ballots = 0
            for prefs in ballots:
                for b in prefs:
                    if b in candidates:
                        counts[b] += 1
                        active_ballots += 1
                        break

            sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

            second_counts = _nth_place_counts(candidates, 1)
            third_counts = _nth_place_counts(candidates, 2)
            fourth_counts = _nth_place_counts(candidates, 3)

            round_info = {
                "counts": {b: c for b, c in sorted_counts},
                "counts_2nd": {b: second_counts.get(b, 0) for b, _ in sorted_counts},
                "counts_3rd": {b: third_counts.get(b, 0) for b, _ in sorted_counts},
                "counts_4th": {b: fourth_counts.get(b, 0) for b, _ in sorted_counts},
                "active_ballots": active_ballots,
            }

            if sorted_counts and active_ballots > 0:
                top_book, top_votes = sorted_counts[0]
                if top_votes > active_ballots / 2 or len(candidates) <= 2:
                    if len(candidates) == 2 and len(sorted_counts) == 2:
                        b1, v1 = sorted_counts[0]
                        b2, v2 = sorted_counts[1]
                        if v1 == v2:
                            resolved = False
                            for rp in [1, 2, 3]:
                                pc = _nth_place_counts({b1, b2}, rp)
                                if pc[b1] != pc[b2]:
                                    top_book = b1 if pc[b1] > pc[b2] else b2
                                    round_info["tiebreak_used"] = rp + 1
                                    resolved = True
                                    break
                            if not resolved:
                                round_info["tied_winners"] = [b1, b2]
                                rounds.append(round_info)
                                ranking = eliminated_order + [b1, b2]
                                break
                    round_info["winner"] = top_book
                    rounds.append(round_info)
                    remaining = [b for b, _ in sorted_counts if b != top_book]

                    def _rank_key(book):
                        fc = counts.get(book, 0)
                        s2 = _nth_place_counts([book], 1).get(book, 0)
                        s3 = _nth_place_counts([book], 2).get(book, 0)
                        s4 = _nth_place_counts([book], 3).get(book, 0)
                        return (fc, s2, s3, s4)

                    remaining.sort(key=_rank_key)
                    ranking = eliminated_order + remaining + [top_book]
                    break

            if sorted_counts:
                min_votes = sorted_counts[-1][1]
                tied_last = [b for b, c in sorted_counts if c == min_votes]

                if len(tied_last) > 1:
                    for rank_pos in [1, 2, 3]:
                        pos_counts = _nth_place_counts(tied_last, rank_pos)
                        min_pos = min(pos_counts.values())
                        still_tied = [b for b, c in pos_counts.items() if c == min_pos]
                        if len(still_tied) < len(tied_last):
                            tied_last = still_tied
                            round_info["tiebreak_used"] = rank_pos + 1
                            if len(tied_last) == 1:
                                break

                remaining_after = len(candidates) - len(tied_last)
                if remaining_after < 2 and len(tied_last) > 1 and len(candidates) > 2:
                    num_to_elim = len(candidates) - 2
                    backup_scores = {}
                    for b in tied_last:
                        score = sum(_nth_place_counts([b], rp).get(b, 0) for rp in [1, 2, 3])
                        backup_scores[b] = score
                    sorted_by_backup = sorted(tied_last, key=lambda b: backup_scores[b])
                    tied_last = sorted_by_backup[:num_to_elim]
                    if not round_info.get("tiebreak_used"):
                        round_info["tiebreak_used"] = "backup"

                if len(tied_last) == len(candidates):
                    round_info["tied_winners"] = list(candidates)
                    rounds.append(round_info)
                    ranking = eliminated_order + [b for b, _ in sorted_counts]
                    break

                round_info["eliminated"] = tied_last[0] if len(tied_last) == 1 else tied_last
                for b in (tied_last if isinstance(tied_last, list) else [tied_last]):
                    candidates.discard(b)
                    eliminated_order.append(b)
            else:
                break

            rounds.append(round_info)

        voter_names = [row.voter_name for row in rows]
        return {
            "vetoed": sorted(vetoed),
            "rounds": rounds,
            "ranking": ranking,
            "total_ballots": len(ballots),
            "voters": voter_names,
        }
    finally:
        db.close()


def get_all_ballots() -> List[Dict]:
    """Return every ballot with voter name and choices."""
    db = SessionLocal()
    try:
        rows = db.query(BookVote).order_by(BookVote.created_at).all()
        results = []
        for row in rows:
            try:
                ballot = _json.loads(row.vote_data)
            except Exception:
                continue
            results.append({
                "voter": row.voter_name,
                "rank1": ballot.get("rank1"),
                "rank2": ballot.get("rank2"),
                "rank3": ballot.get("rank3"),
                "rank4": ballot.get("rank4"),
                "veto": ballot.get("veto"),
            })
        return results
    finally:
        db.close()


def delete_ballot_by_name(voter_name: str) -> bool:
    db = SessionLocal()
    try:
        row = db.query(BookVote).filter(BookVote.voter_name == voter_name).first()
        if not row:
            return False
        db.delete(row)
        db.commit()
        return True
    finally:
        db.close()


def get_vote_cards() -> List[Dict]:
    db = SessionLocal()
    try:
        rows = db.query(VoteCard).order_by(VoteCard.created_at.desc()).all()
        return [
            {
                "id": r.id,
                "author": r.author,
                "text": r.text,
                "created_at": r.created_at.isoformat(),
            }
            for r in rows
        ]
    finally:
        db.close()


def add_vote_card(author: str, text: str) -> Dict:
    db = SessionLocal()
    try:
        card = VoteCard(author=author, text=text)
        db.add(card)
        db.commit()
        db.refresh(card)
        return {
            "id": card.id,
            "author": card.author,
            "text": card.text,
            "created_at": card.created_at.isoformat(),
        }
    finally:
        db.close()


def delete_vote_card(card_id: int) -> bool:
    db = SessionLocal()
    try:
        card = db.query(VoteCard).filter(VoteCard.id == card_id).first()
        if not card:
            return False
        db.delete(card)
        db.commit()
        return True
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Books — ballot candidates, suggestions, and round history.

# The list that was hardcoded in the frontend before books moved to the DB.
# Seeded once so the round in progress at deploy time keeps working.
LEGACY_BOOKS = [
    {"title": "America's Constitution: A Biography", "author": "Akhil Reed Amar", "pages": 657, "description": "A comprehensive, entertaining account of what the Constitution says and why it says it, by one of the era's leading constitutional law scholars.", "url": "https://www.goodreads.com/book/show/843764.America_s_Constitution"},
    {"title": "Americanos", "author": "John Charles Chasteen", "pages": 206, "description": "A vivid, cinematic history of Latin America's wars of independence, from Bolivar and San Martin to lesser-known patriots who shaped nineteen new republics.", "url": "https://www.goodreads.com/book/show/2433911.Americanos"},
    {"title": "A Sand County Almanac", "author": "Aldo Leopold", "pages": 228, "description": "A landmark of the conservation movement, these essays advocate a 'land ethic' -- a responsible relationship between people and the land they inhabit.", "url": "https://www.goodreads.com/book/show/210404.A_Sand_County_Almanac_and_Sketches_Here_and_There"},
    {"title": "Whale", "author": "Cheon Myeong-kwan", "pages": 320, "description": "A magical realist Korean novel following three extraordinary women -- one who chases whales, her elephant-whispering daughter, and a one-eyed beekeeper. Shortlisted for the International Booker Prize.", "url": "https://www.goodreads.com/book/show/29382499-whale"},
    {"title": "Caste", "author": "Isabel Wilkerson", "pages": 496, "description": "Examines American racism as a caste system, drawing parallels with India and Nazi Germany to reveal how hierarchy, exclusion, and purity shape societies.", "url": "https://www.goodreads.com/book/show/51152447-caste"},
    {"title": "Frederick Douglass: Prophet of Freedom", "author": "David W. Blight", "pages": 912, "description": "The definitive biography of the abolitionist, writer, and orator, drawing on new sources to capture Douglass's extraordinary life. Winner of the 2019 Pulitzer Prize for History.", "url": "https://www.goodreads.com/book/show/38530663-frederick-douglass"},
    {"title": "The Radicalism of the American Revolution", "author": "Gordon S. Wood", "pages": 447, "description": "Argues the Revolution was far more radical than previously understood, fundamentally transforming American society from monarchy to democracy. Winner of the 1993 Pulitzer Prize.", "url": "https://www.goodreads.com/book/show/6956.The_Radicalism_of_the_American_Revolution"},
    {"title": "Black Reconstruction in America", "author": "W. E. B. Du Bois", "pages": 746, "description": "A groundbreaking 1935 history that challenged prevailing narratives by centering Black agency during the Civil War and Reconstruction, revealing the era's democratic promise.", "url": "https://www.goodreads.com/book/show/184612.Black_Reconstruction_in_America_1860_1880"},
    {"title": "Parting the Waters", "author": "Taylor Branch", "pages": 1064, "description": "The first volume of Branch's epic trilogy on MLK and the Civil Rights movement, covering the Montgomery boycott through the 1963 March on Washington. Pulitzer Prize winner.", "url": "https://www.goodreads.com/book/show/99199.Parting_the_Waters"},
    {"title": "A Clearing in the Distance", "author": "Witold Rybczynski", "pages": 352, "description": "Biography of Frederick Law Olmsted, designer of Central Park and Boston's Emerald Necklace, who was also a journalist whose dispatches on slavery became essential American documents.", "url": "https://www.goodreads.com/book/show/344846.A_Clearing_in_the_Distance"},
    {"title": "The Great Leveler", "author": "Walter Scheidel", "pages": 504, "description": "Argues that throughout history, only catastrophic violence -- mass warfare, revolution, state collapse, and plague -- has significantly reduced economic inequality.", "url": "https://www.goodreads.com/book/show/31951505-the-great-leveler"},
    {"title": "Material World", "author": "Ed Conway", "pages": 512, "description": "A vivid account of the six raw materials — sand, salt, iron, copper, oil, and lithium — that underpin modern civilization, tracing them from mine to the products we can't live without.", "url": "https://www.goodreads.com/book/show/125937631-material-world"},
]


def _book_to_dict(b: Book) -> Dict:
    return {
        "id": b.id,
        "title": b.title,
        "author": b.author,
        "pages": b.pages,
        "desc": b.description or "",
        "url": b.url or "",
        "status": b.status,
        "suggested_by": b.suggested_by,
        "created_at": b.created_at.isoformat() if b.created_at else None,
    }


def seed_books_if_empty() -> int:
    """Seed the legacy hardcoded ballot once. Idempotent."""
    db = SessionLocal()
    try:
        if db.query(Book).count() > 0:
            return 0
        for b in LEGACY_BOOKS:
            db.add(Book(
                title=b["title"], author=b["author"], pages=b.get("pages"),
                description=b.get("description"), url=b.get("url"), status="active",
            ))
        db.commit()
        return len(LEGACY_BOOKS)
    except Exception as e:
        db.rollback()
        logger.error(f"seed_books_if_empty failed: {e}")
        return 0
    finally:
        db.close()


def get_books(status: Optional[str] = None) -> List[Dict]:
    db = SessionLocal()
    try:
        q = db.query(Book)
        if status:
            q = q.filter(Book.status == status)
        return [_book_to_dict(b) for b in q.order_by(Book.created_at).all()]
    finally:
        db.close()


def _find_duplicate_title(db, title: str) -> Optional[Book]:
    """Case-insensitive title match among non-archived books."""
    t = title.strip().lower()
    for b in db.query(Book).filter(Book.status != "archived").all():
        if b.title.strip().lower() == t:
            return b
    return None


def add_book(
    title: str,
    author: str,
    pages: Optional[int] = None,
    description: Optional[str] = None,
    url: Optional[str] = None,
    status: str = "active",
    suggested_by: Optional[str] = None,
) -> Dict:
    db = SessionLocal()
    try:
        if _find_duplicate_title(db, title):
            return {"success": False, "reason": "duplicate"}
        book = Book(
            title=title.strip(), author=author.strip(), pages=pages,
            description=description, url=url, status=status, suggested_by=suggested_by,
        )
        db.add(book)
        db.commit()
        db.refresh(book)
        return {"success": True, "book": _book_to_dict(book)}
    except Exception as e:
        db.rollback()
        logger.error(f"add_book failed: {e}")
        return {"success": False, "reason": "error"}
    finally:
        db.close()


def update_book(book_id: int, fields: Dict) -> Optional[Dict]:
    """Update title/author/pages/description/url/status. Returns None if missing."""
    db = SessionLocal()
    try:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            return None
        for attr in ("title", "author", "pages", "description", "url", "status"):
            if attr in fields and fields[attr] is not None:
                setattr(book, attr, fields[attr])
        db.commit()
        db.refresh(book)
        return _book_to_dict(book)
    except Exception as e:
        db.rollback()
        logger.error(f"update_book failed: {e}")
        return None
    finally:
        db.close()


def book_has_ballots(book_id: int) -> bool:
    """True if any current ballot ranks or vetoes this book (by title)."""
    db = SessionLocal()
    try:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            return False
        title = book.title
        for row in db.query(BookVote).all():
            try:
                ballot = _json.loads(row.vote_data)
            except Exception:
                continue
            if title in (ballot.get("rank1"), ballot.get("rank2"),
                         ballot.get("rank3"), ballot.get("rank4"), ballot.get("veto")):
                return True
        return False
    finally:
        db.close()


def delete_book(book_id: int) -> str:
    """Returns 'ok', 'not_found', or 'blocked' (referenced by a live ballot)."""
    if book_has_ballots(book_id):
        return "blocked"
    db = SessionLocal()
    try:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            return "not_found"
        db.delete(book)
        db.commit()
        return "ok"
    finally:
        db.close()


def reset_round(label: Optional[str] = None) -> Dict:
    """Close the current round: snapshot everything into VoteRound, then
    clear ballots + cards and archive all active books. Suggestions survive.
    Skips the snapshot (nothing to preserve) when there are no ballots."""
    results = get_vote_results()
    ballots = get_all_ballots()
    cards = get_vote_cards()
    active_books = get_books("active")
    db = SessionLocal()
    try:
        summary: Dict = {"success": True, "archived_round": False, "winner": None}
        if ballots:
            ranking = results.get("ranking") or []
            winner = ranking[-1] if ranking else None
            snapshot = {
                "label": label,
                "books": active_books,
                "ballots": ballots,
                "results": results,
                "cards": cards,
                "winner": winner,
            }
            db.add(VoteRound(
                label=label, winner=winner, total_ballots=len(ballots),
                snapshot=_json.dumps(snapshot),
            ))
            summary["archived_round"] = True
            summary["winner"] = winner
        summary["ballots_cleared"] = db.query(BookVote).delete()
        summary["cards_cleared"] = db.query(VoteCard).delete()
        summary["books_archived"] = (
            db.query(Book).filter(Book.status == "active").update({"status": "archived"})
        )
        db.commit()
        return summary
    except Exception as e:
        db.rollback()
        logger.error(f"reset_round failed: {e}")
        return {"success": False, "reason": "error"}
    finally:
        db.close()


def get_rounds() -> List[Dict]:
    """History listing, newest first. Summaries only — no full snapshots."""
    db = SessionLocal()
    try:
        rows = db.query(VoteRound).order_by(VoteRound.created_at.desc()).all()
        return [
            {
                "id": r.id,
                "label": r.label,
                "winner": r.winner,
                "total_ballots": r.total_ballots,
                "created_at": r.created_at.isoformat() if r.created_at else None,
            }
            for r in rows
        ]
    finally:
        db.close()


def get_round(round_id: int) -> Optional[Dict]:
    db = SessionLocal()
    try:
        r = db.query(VoteRound).filter(VoteRound.id == round_id).first()
        if not r:
            return None
        try:
            snapshot = _json.loads(r.snapshot)
        except Exception:
            snapshot = {}
        snapshot["id"] = r.id
        snapshot["created_at"] = r.created_at.isoformat() if r.created_at else None
        return snapshot
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Seed helpers — used once on first boot to migrate data from Life.


def seed_if_empty(seed_data: Dict) -> Dict:
    """
    If no ballots exist yet, load from a dict of:
      {"ballots": [{voter, rank1, rank2, rank3, rank4, veto}, ...],
       "cards": [{author, text, created_at (iso)}, ...]}

    Idempotent — won't overwrite once any vote exists.
    """
    db = SessionLocal()
    summary = {"ballots_inserted": 0, "cards_inserted": 0, "skipped": False}
    try:
        existing = db.query(BookVote).count()
        if existing > 0:
            summary["skipped"] = True
            return summary
        for b in seed_data.get("ballots") or []:
            voter = b.get("voter")
            if not voter:
                continue
            payload = {
                "rank1": b.get("rank1"),
                "rank2": b.get("rank2"),
                "rank3": b.get("rank3"),
                "rank4": b.get("rank4"),
                "veto": b.get("veto"),
            }
            db.add(BookVote(voter_name=voter, vote_data=_json.dumps(payload)))
            summary["ballots_inserted"] += 1
        for c in seed_data.get("cards") or []:
            author = c.get("author") or "Anonymous"
            text = c.get("text")
            if not text:
                continue
            created = c.get("created_at")
            card = VoteCard(author=author, text=text)
            if created:
                try:
                    card.created_at = datetime.fromisoformat(created)
                except Exception:
                    pass
            db.add(card)
            summary["cards_inserted"] += 1
        db.commit()
        return summary
    except Exception as e:
        db.rollback()
        logger.error(f"seed_if_empty failed: {e}")
        summary["error"] = str(e)
        return summary
    finally:
        db.close()
