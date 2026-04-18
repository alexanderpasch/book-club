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
