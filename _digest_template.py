# Auto-extracted from Life's backend/main.py (digest template wrapper).
from jinja2 import Template

_DIGEST_TEMPLATE = Template(
    """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ title }}</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #0f172a;
      --panel: #111827;
      --muted: #94a3b8;
      --text: #e5e7eb;
      --accent: #38bdf8;
      --accent-soft: rgba(56, 189, 248, 0.14);
      --border: rgba(148, 163, 184, 0.18);
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
      color: var(--text);
    }
    .shell {
      max-width: 920px;
      margin: 0 auto;
      padding: 24px 16px 56px;
    }
    .card {
      background: rgba(15, 23, 42, 0.92);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 20px;
      box-shadow: 0 18px 42px rgba(2, 6, 23, 0.28);
      backdrop-filter: blur(10px);
    }
    .topbar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 18px;
    }
    .eyebrow {
      color: var(--accent);
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 8px;
    }
    h1 {
      margin: 0;
      font-size: clamp(1.7rem, 4vw, 2.4rem);
      line-height: 1.1;
    }
    .meta {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 14px;
    }
    .chip {
      padding: 8px 12px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: rgba(30, 41, 59, 0.88);
      color: var(--muted);
      font-size: 0.9rem;
    }
    .nav {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 18px;
    }
    .nav a {
      text-decoration: none;
      color: var(--text);
      background: var(--accent-soft);
      border: 1px solid rgba(56, 189, 248, 0.28);
      padding: 10px 14px;
      border-radius: 999px;
      font-size: 0.95rem;
    }
    .summary {
      margin-top: 36px;
      display: grid;
      gap: 14px;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    }
    .section-title {
      margin: 28px 0 12px;
      font-size: 1.05rem;
      color: var(--muted);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
    .digest-intro {
      margin: 10px 0 0;
      color: var(--muted);
      line-height: 1.6;
      max-width: 760px;
    }
    .summary .panel {
      padding: 16px;
      border-radius: 14px;
      border: 1px solid var(--border);
      background: rgba(15, 23, 42, 0.72);
    }
    .summary .label {
      color: var(--muted);
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 6px;
    }
    .summary .value {
      font-size: 1rem;
      line-height: 1.5;
      word-break: break-word;
    }
    ol.digest {
      margin: 24px 0 0;
      padding: 0;
      list-style: none;
      display: grid;
      gap: 12px;
    }
    .item {
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 16px;
      background: rgba(15, 23, 42, 0.75);
    }
    .item-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
      margin-bottom: 8px;
    }
    .item-head-main {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }
    .item-actions {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-left: auto;
    }
    .item-num {
      width: 34px;
      height: 34px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 999px;
      background: rgba(56, 189, 248, 0.18);
      color: var(--accent);
      font-weight: 700;
    }
    .item-cat {
      color: var(--muted);
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
    .item-text {
      margin: 0;
      line-height: 1.65;
      white-space: pre-wrap;
    }
    .item-summary {
      margin: 10px 0 0;
      color: var(--muted);
      line-height: 1.6;
      white-space: pre-wrap;
    }
    .expandable {
      margin-top: 10px;
    }
    .expandable .item-summary {
      margin-top: 0;
    }
    .expandable-preview {
      display: inline;
    }
    .expandable-full {
      display: none;
    }
    .expandable.is-expanded .expandable-preview {
      display: none;
    }
    .expandable.is-expanded .expandable-full {
      display: inline;
    }
    .expand-toggle {
      margin-top: 8px;
      padding: 0;
      border: 0;
      background: transparent;
      color: var(--accent);
      font: inherit;
      cursor: pointer;
    }
    .item-query {
      margin-top: 12px;
      color: var(--muted);
      font-size: 0.9rem;
      line-height: 1.5;
    }
    .item-sources {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 12px;
    }
    .source-link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      color: var(--accent);
      border: 1px solid rgba(56, 189, 248, 0.22);
      background: rgba(56, 189, 248, 0.08);
      padding: 8px 12px;
      border-radius: 999px;
      font-size: 0.92rem;
    }
    .item-action-link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      color: var(--text);
      border: 1px solid rgba(148, 163, 184, 0.2);
      background: rgba(30, 41, 59, 0.88);
      padding: 8px 12px;
      border-radius: 999px;
      font-size: 0.9rem;
      white-space: nowrap;
    }
    .item-action-link:hover {
      border-color: rgba(56, 189, 248, 0.34);
      background: rgba(56, 189, 248, 0.12);
    }
    .rating-block {
      margin-top: 16px;
      padding-top: 14px;
      border-top: 1px solid rgba(148, 163, 184, 0.14);
    }
    .rating-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 12px;
    }
    .rating-scale {
      padding: 12px 14px;
      border-radius: 14px;
      border: 1px solid rgba(148, 163, 184, 0.14);
      background: rgba(15, 23, 42, 0.58);
    }
    .scale-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 8px;
    }
    .scale-title {
      color: var(--muted);
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
    .scale-value {
      min-width: 28px;
      text-align: center;
      font-weight: 700;
      color: var(--accent);
    }
    .scale-input {
      width: 100%;
      accent-color: #38bdf8;
    }
    .rating-status {
      margin-top: 10px;
      min-height: 1.2em;
      color: var(--muted);
      font-size: 0.9rem;
    }
    .rating-status[data-state="saved"] {
      color: #86efac;
    }
    .rating-status[data-state="error"] {
      color: #fca5a5;
    }
    .metadata-block {
      margin-top: 12px;
    }
    .history {
      display: grid;
      gap: 12px;
      margin-top: 24px;
    }
    .history a {
      display: block;
      color: inherit;
      text-decoration: none;
    }
    .history .entry {
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 16px;
      background: rgba(15, 23, 42, 0.75);
    }
    .history .entry:hover {
      border-color: rgba(56, 189, 248, 0.34);
      transform: translateY(-1px);
    }
    .muted {
      color: var(--muted);
    }
    .empty {
      margin-top: 24px;
      padding: 24px;
      border-radius: 16px;
      border: 1px dashed var(--border);
      color: var(--muted);
      text-align: center;
    }
    @media (max-width: 640px) {
      .shell { padding: 18px 12px 40px; }
      .card { padding: 16px; }
      .item { padding: 14px; }
    }
  </style>
</head>
<body>
  <div class="shell">
    <div class="card">
      {{ body|safe }}
    </div>
  </div>
  <script>
    (() => {
      async function saveRating(card) {
        const status = card.querySelector('.rating-status');
        const interesting = card.querySelector('[data-field="interesting_score"]');
        const currentness = card.querySelector('[data-field="currentness_score"]');
        status.dataset.state = 'saving';
        status.textContent = 'Saving…';
        try {
          const response = await fetch('/digest/rate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              digest_id: Number(card.dataset.digestId),
              chat_id: Number(card.dataset.chatId),
              item_number: Number(card.dataset.itemNumber),
              interesting_score: Number(interesting.value),
              currentness_score: Number(currentness.value),
            }),
          });
          const payload = await response.json();
          if (!response.ok || !payload.success) {
            throw new Error(payload.error || 'Could not save rating');
          }
          status.dataset.state = 'saved';
          status.textContent = 'Saved';
        } catch (error) {
          status.dataset.state = 'error';
          status.textContent = error.message || 'Could not save';
        }
      }

      function bindCard(card) {
        const inputs = card.querySelectorAll('.scale-input');
        inputs.forEach((input) => {
          const valueNode = card.querySelector(`[data-value-for="${input.dataset.field}"]`);
          const syncValue = () => {
            if (valueNode) valueNode.textContent = input.value;
          };
          input.addEventListener('input', syncValue);
          input.addEventListener('change', () => saveRating(card));
          syncValue();
        });
      }

      function bindExpandable(block) {
        const button = block.querySelector('.expand-toggle');
        if (!button) return;
        button.addEventListener('click', () => {
          const expanded = block.classList.toggle('is-expanded');
          button.textContent = expanded ? 'Show less' : 'Show more';
          button.setAttribute('aria-expanded', expanded ? 'true' : 'false');
        });
      }

      document.querySelectorAll('.item-rating').forEach(bindCard);
      document.querySelectorAll('[data-expandable="true"]').forEach(bindExpandable);
    })();
  </script>
</body>
</html>
    """
)
