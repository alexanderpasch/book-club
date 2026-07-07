"""
Book Club — standalone FastAPI service.

Originally a subroute of the Life project (https://life-production-a332.up.railway.app/vote);
moved to its own Railway project/domain so the personal Life stack stays
private and isolated.

Routes:
  GET  /                      → redirect to /vote
  GET  /vote                  → voting HTML page
  POST /vote/submit           → submit/upsert a ballot
  GET  /vote/results/data     → JSON results (public)
  GET  /vote/books            → active (votable) books
  GET  /vote/suggestions      → pending user suggestions
  POST /vote/suggest          → suggest a book (public)
  POST /vote/books?password   → add a book directly (admin)
  PUT  /vote/books/{id}?password    → edit a book (admin)
  DELETE /vote/books/{id}?password  → remove a book/suggestion (admin)
  POST /vote/books/{id}/approve?password → suggestion → ballot (admin)
  POST /vote/admin/check?password   → verify admin password for UI unlock
  POST /vote/reset?password   → archive round to history + clear (admin)
  GET  /vote/history          → past rounds (summaries)
  GET  /vote/history/{id}     → full frozen snapshot of a past round
  GET  /vote/cards            → list waiting-room cards
  POST /vote/cards            → create a card
  DELETE /vote/cards/{id}     → delete a card
  POST /vote/ballots?password → export all ballots (password-gated)
  DELETE /vote/ballot/{name}  → delete a specific ballot (password-gated)
  GET  /health                → health check
  POST /_admin/seed           → one-shot migration from Life (token-gated)
"""

import json
import logging
import os
from typing import Optional

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel

from database import (
    add_book,
    add_vote_card,
    delete_ballot_by_name,
    delete_book,
    delete_vote_card,
    get_all_ballots,
    get_books,
    get_round,
    get_rounds,
    get_vote_cards,
    get_vote_results,
    init_db,
    reset_round,
    seed_books_if_empty,
    seed_if_empty,
    update_book,
    upsert_book_vote,
)

# Template and body lifted verbatim from Life's backend/main.py.
from _digest_template import _DIGEST_TEMPLATE  # type: ignore
from _vote_body import _BOOK_VOTE_BODY  # type: ignore

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("book-club")

BALLOT_PASSWORD = os.getenv("BALLOT_PASSWORD", "bookclub2026")
ADMIN_SEED_TOKEN = os.getenv("ADMIN_SEED_TOKEN")  # required to hit /_admin/seed

app = FastAPI(title="Book Club")


@app.on_event("startup")
def _startup() -> None:
    init_db()
    seeded = seed_books_if_empty()
    if seeded:
        logger.info(f"Seeded {seeded} legacy books into books table")
    logger.info("Book Club DB initialized")


def _require_password(password: str) -> None:
    if password != BALLOT_PASSWORD:
        raise HTTPException(status_code=403, detail="Wrong password.")


def _render_page(title: str, body: str) -> HTMLResponse:
    return HTMLResponse(_DIGEST_TEMPLATE.render(title=title, body=body))


# ---------------------------------------------------------------------------
# Public routes


@app.get("/")
async def root():
    return RedirectResponse(url="/vote", status_code=302)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/vote", response_class=HTMLResponse)
async def book_vote():
    return _render_page("Book Vote", _BOOK_VOTE_BODY)


class VoteSubmitRequest(BaseModel):
    display_name: str
    rank1: str
    rank2: str
    rank3: str
    rank4: str
    veto: Optional[str] = None


@app.post("/vote/submit")
async def submit_vote(payload: VoteSubmitRequest, request: Request):
    voter_name = payload.display_name.strip()
    if not voter_name:
        raise HTTPException(status_code=400, detail="Name is required.")
    result = upsert_book_vote(
        voter_name,
        {
            "rank1": payload.rank1,
            "rank2": payload.rank2,
            "rank3": payload.rank3,
            "rank4": payload.rank4,
            "veto": payload.veto,
        },
    )
    if not result["success"]:
        raise HTTPException(status_code=500, detail="Could not save vote.")
    return {"success": True, "updated": result["updated"]}


@app.get("/vote/results/data")
async def vote_results_data():
    return get_vote_results()


@app.post("/vote/ballots")
async def vote_ballots(password: str = Query(...)):
    if password != BALLOT_PASSWORD:
        raise HTTPException(status_code=403, detail="Wrong password.")
    return {"ballots": get_all_ballots()}


@app.delete("/vote/ballot/{voter_name}")
async def delete_ballot(voter_name: str, password: str = Query(...)):
    if password != BALLOT_PASSWORD:
        raise HTTPException(status_code=403, detail="Wrong password.")
    if not delete_ballot_by_name(voter_name):
        raise HTTPException(status_code=404, detail="Vote not found.")
    return {"deleted": voter_name}


class CardSubmitRequest(BaseModel):
    author: str
    text: str


@app.get("/vote/cards")
async def list_vote_cards():
    return {"cards": get_vote_cards()}


@app.post("/vote/cards")
async def create_vote_card(payload: CardSubmitRequest):
    author = payload.author.strip()
    text = payload.text.strip()
    if not author or not text:
        raise HTTPException(status_code=400, detail="Author and text are required.")
    if len(text) > 280:
        raise HTTPException(status_code=400, detail="Card text must be 280 characters or fewer.")
    card = add_vote_card(author, text)
    return {"success": True, "card": card}


@app.delete("/vote/cards/{card_id}")
async def remove_vote_card(card_id: int):
    if not delete_vote_card(card_id):
        raise HTTPException(status_code=404, detail="Card not found.")
    return {"success": True}


# ---------------------------------------------------------------------------
# Books — dynamic ballot, suggestions, and round history.


class SuggestRequest(BaseModel):
    title: str
    author: str
    url: Optional[str] = None
    note: Optional[str] = None  # "why this book" — stored as the description
    suggested_by: Optional[str] = None


class BookCreateRequest(BaseModel):
    title: str
    author: str
    pages: Optional[int] = None
    desc: Optional[str] = None
    url: Optional[str] = None


class BookUpdateRequest(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    pages: Optional[int] = None
    desc: Optional[str] = None
    url: Optional[str] = None


@app.get("/vote/books")
async def list_books():
    """Active (votable) books — the ballot the page renders."""
    return {"books": get_books("active")}


@app.get("/vote/suggestions")
async def list_suggestions():
    """Pending suggestions, publicly visible but not votable."""
    return {"suggestions": get_books("suggested")}


@app.post("/vote/suggest")
async def suggest_book(payload: SuggestRequest):
    title = payload.title.strip()
    author = payload.author.strip()
    if not title or not author:
        raise HTTPException(status_code=400, detail="Title and author are required.")
    result = add_book(
        title=title,
        author=author,
        url=(payload.url or "").strip() or None,
        description=(payload.note or "").strip() or None,
        status="suggested",
        suggested_by=(payload.suggested_by or "").strip() or None,
    )
    if not result["success"]:
        if result.get("reason") == "duplicate":
            raise HTTPException(status_code=409, detail="That book is already on the ballot or suggested.")
        raise HTTPException(status_code=500, detail="Could not save suggestion.")
    return result


@app.post("/vote/books")
async def create_book(payload: BookCreateRequest, password: str = Query(...)):
    _require_password(password)
    title = payload.title.strip()
    author = payload.author.strip()
    if not title or not author:
        raise HTTPException(status_code=400, detail="Title and author are required.")
    result = add_book(
        title=title, author=author, pages=payload.pages,
        description=payload.desc, url=payload.url, status="active",
    )
    if not result["success"]:
        if result.get("reason") == "duplicate":
            raise HTTPException(status_code=409, detail="That book is already on the ballot or suggested.")
        raise HTTPException(status_code=500, detail="Could not add book.")
    return result


@app.put("/vote/books/{book_id}")
async def edit_book(book_id: int, payload: BookUpdateRequest, password: str = Query(...)):
    _require_password(password)
    fields = {
        "title": (payload.title or "").strip() or None,
        "author": (payload.author or "").strip() or None,
        "pages": payload.pages,
        "description": payload.desc,
        "url": payload.url,
    }
    book = update_book(book_id, fields)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found.")
    return {"success": True, "book": book}


@app.delete("/vote/books/{book_id}")
async def remove_book(book_id: int, password: str = Query(...)):
    _require_password(password)
    outcome = delete_book(book_id)
    if outcome == "not_found":
        raise HTTPException(status_code=404, detail="Book not found.")
    if outcome == "blocked":
        raise HTTPException(
            status_code=409,
            detail="Someone already voted for this book. Reset the round to remove it.",
        )
    return {"success": True}


@app.post("/vote/books/{book_id}/approve")
async def approve_book(book_id: int, password: str = Query(...)):
    _require_password(password)
    book = update_book(book_id, {"status": "active"})
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found.")
    return {"success": True, "book": book}


@app.post("/vote/admin/check")
async def admin_check(password: str = Query(...)):
    _require_password(password)
    return {"ok": True}


@app.post("/vote/reset")
async def reset_vote(password: str = Query(...)):
    _require_password(password)
    summary = reset_round()
    if not summary.get("success"):
        raise HTTPException(status_code=500, detail="Reset failed.")
    logger.info(f"Round reset: {summary}")
    return summary


@app.get("/vote/history")
async def vote_history():
    return {"rounds": get_rounds()}


@app.get("/vote/history/{round_id}")
async def vote_history_detail(round_id: int):
    snapshot = get_round(round_id)
    if snapshot is None:
        raise HTTPException(status_code=404, detail="Round not found.")
    return snapshot


# ---------------------------------------------------------------------------
# One-shot admin route — used once to import ballots+cards exported from Life.
# Requires ADMIN_SEED_TOKEN env var. Idempotent: skips if any ballots exist.


class SeedRequest(BaseModel):
    ballots: list = []
    cards: list = []


@app.post("/_admin/seed")
async def admin_seed(payload: SeedRequest, token: str = Query(...)):
    if not ADMIN_SEED_TOKEN:
        raise HTTPException(status_code=503, detail="Seeding disabled (ADMIN_SEED_TOKEN unset).")
    if token != ADMIN_SEED_TOKEN:
        raise HTTPException(status_code=403, detail="Wrong token.")
    summary = seed_if_empty({"ballots": payload.ballots, "cards": payload.cards})
    return summary
