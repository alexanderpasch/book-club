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
    add_vote_card,
    delete_ballot_by_name,
    delete_vote_card,
    get_all_ballots,
    get_vote_cards,
    get_vote_results,
    init_db,
    seed_if_empty,
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
    logger.info("Book Club DB initialized")


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
