# Book Club

> ATX Book Club

Standalone voting site for an in-person book club. Ranked-choice ballots + a waiting-room carousel of user-submitted cards.

Originally lived inside the Life project at `https://life-production-a332.up.railway.app/vote`. Extracted to its own Railway project + GitHub repo in April 2026 to decouple from personal systems. The old URL now redirects here.

## Stack

- FastAPI + uvicorn
- SQLAlchemy + SQLite on a Railway volume (`/app/data/book_club.db`)
- Inline Jinja2 template (no build step)

## Local development

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
# http://localhost:8000/vote
```

## Environment variables

| Name | Purpose | Default |
|---|---|---|
| `BALLOT_PASSWORD` | Password to export ballots (`POST /vote/ballots`) and delete a vote | `bookclub2026` |
| `ADMIN_SEED_TOKEN` | Token for one-shot `POST /_admin/seed` migration endpoint | unset (endpoint disabled) |
| `DATABASE_URL` | Override DB URL (otherwise SQLite at `$RAILWAY_VOLUME_MOUNT_PATH/book_club.db`) | unset |
| `BOOK_CLUB_DB_PATH` | Override SQLite path directly | unset |

## Routes

| Method | Path | Auth |
|---|---|---|
| GET | `/` | — (redirect to `/vote`) |
| GET | `/vote` | — |
| POST | `/vote/submit` | — |
| GET | `/vote/results/data` | — |
| GET | `/vote/cards` | — |
| POST | `/vote/cards` | — |
| DELETE | `/vote/cards/{id}` | — |
| POST | `/vote/ballots?password=…` | password |
| DELETE | `/vote/ballot/{name}?password=…` | password |
| GET | `/health` | — |
| POST | `/_admin/seed?token=…` | token (one-shot migration) |

## One-shot migration from Life

```bash
# On Life side — export data (already done and saved in /tmp/bookclub-migrate/):
curl -X POST "https://life-production-a332.up.railway.app/vote/ballots?password=bookclub2026" > ballots.json
curl "https://life-production-a332.up.railway.app/vote/cards" > cards.json

# On book-club side — POST to the new site:
python3 -c "
import json, urllib.request
ballots = json.load(open('ballots.json'))['ballots']
cards = json.load(open('cards.json'))['cards']
body = json.dumps({'ballots': ballots, 'cards': cards}).encode()
req = urllib.request.Request(
    'https://<new-domain>/_admin/seed?token=<admin-token>',
    data=body, method='POST',
    headers={'Content-Type': 'application/json'},
)
print(urllib.request.urlopen(req).read().decode())
"
```
