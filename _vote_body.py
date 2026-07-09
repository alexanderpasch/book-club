# Auto-extracted from Life's backend/main.py (book-vote body).
_BOOK_VOTE_BODY = """
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400;1,600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='85'%3E%F0%9F%93%9A%3C/text%3E%3C/svg%3E">
<link rel="apple-touch-icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='85'%3E%F0%9F%93%9A%3C/text%3E%3C/svg%3E">
<div class="vote-hero">
  <div class="vote-hero-bg"></div>
  <div class="vote-hero-content">
    <div class="vote-eyebrow">
      <span class="vote-eyebrow-rule"></span>
      <span class="vote-eyebrow-text">Book Club</span>
      <span class="vote-eyebrow-rule"></span>
    </div>
    <h1>Vote for Our<br><em>Next Read</em></h1>
    <div class="vote-ornament">
      <span class="vo-line"></span>
      <span class="vo-glyph">&#10022;</span>
      <span class="vo-line"></span>
    </div>
    <p class="vote-subtitle">Pick your <strong>top 4 choices</strong> &mdash; you can also <strong>optionally</strong> veto one book you&rsquo;d rather skip.</p>
  </div>
</div>

<style>
  /* Book club warm theme — override dark template vars */
  :root {
    color-scheme: light !important;
    --bg: #f5efe6 !important;
    --panel: #fffbf5 !important;
    --muted: #8b7355 !important;
    --text: #2c1810 !important;
    --accent: #7c3a2e !important;
    --accent-soft: rgba(124, 58, 46, 0.08) !important;
    --border: rgba(139, 100, 60, 0.15) !important;
  }
  body {
    background: linear-gradient(180deg, #ede4d4 0%, #f5efe6 40%, #faf7f2 100%) !important;
    color: var(--text) !important;
  }
  .card {
    background: rgba(255, 251, 245, 0.97) !important;
    border: 1px solid rgba(139, 100, 60, 0.12) !important;
    box-shadow: 0 4px 24px rgba(44, 24, 16, 0.06), 0 1px 3px rgba(44, 24, 16, 0.04) !important;
  }
  .shell { max-width: 920px; }

  /* ── Hero Header ─────────────────────────────── */
  .card { overflow: hidden !important; padding: 0 !important; }

  .vote-hero {
    position: relative;
    background: #2a1208;
    padding: 52px 32px 48px;
    text-align: center;
    overflow: hidden;
  }
  /* Subtle radial glow in centre */
  .vote-hero-bg {
    position: absolute; inset: 0; pointer-events: none;
    background: radial-gradient(ellipse 70% 80% at 50% 0%, rgba(180,90,40,0.28) 0%, transparent 70%),
                radial-gradient(ellipse 50% 50% at 80% 100%, rgba(120,50,20,0.18) 0%, transparent 60%);
  }
  .vote-hero-content { position: relative; z-index: 1; }

  .vote-eyebrow {
    display: flex; align-items: center; justify-content: center; gap: 14px;
    margin-bottom: 22px;
  }
  .vote-eyebrow-text {
    font-family: 'Libre Baskerville', Georgia, serif;
    font-size: 0.68rem; letter-spacing: 0.3em; text-transform: uppercase;
    color: #c9956a;
  }
  .vote-eyebrow-rule {
    display: block; width: 36px; height: 1px;
    background: linear-gradient(90deg, transparent, #c9956a);
  }
  .vote-eyebrow-rule:last-child {
    background: linear-gradient(90deg, #c9956a, transparent);
  }

  h1 {
    color: #f5ede0 !important;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(2.8rem, 6.5vw, 4.6rem);
    font-weight: 300;
    letter-spacing: 0.01em;
    line-height: 1.1;
    margin: 0 auto 20px;
  }
  h1 em {
    font-style: italic;
    font-weight: 300;
    color: #d4956a;
  }

  .vote-ornament {
    display: flex; align-items: center; justify-content: center; gap: 14px;
    margin: 0 auto 24px;
  }
  .vo-line {
    display: block; width: 48px; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(201,149,106,0.5));
  }
  .vo-line:last-child {
    background: linear-gradient(90deg, rgba(201,149,106,0.5), transparent);
  }
  .vo-glyph {
    color: #c9956a; font-size: 10px; opacity: 0.7;
  }

  .vote-subtitle {
    font-family: 'Libre Baskerville', Georgia, serif;
    font-size: 0.88rem; line-height: 1.8; color: rgba(245,237,224,0.65);
    margin: 0 auto; max-width: 520px; text-align: center;
  }
  .vote-subtitle strong { color: rgba(245,237,224,0.9); font-weight: 700; }

  /* Content area below hero gets its own padding */
  .vote-content-area { padding: 0 20px 32px; }
  @media (min-width: 601px) {
    .vote-content-area { padding: 0 28px 40px; }
    .vote-hero { padding: 60px 48px 56px; }
    h1 { font-size: clamp(3.2rem, 5.5vw, 5rem); }
    .vote-subtitle { font-size: 0.95rem; }
  }

  .chip { background: rgba(139, 100, 60, 0.08) !important; color: var(--muted) !important; border-color: var(--border) !important; }
  .nav a { background: var(--accent-soft) !important; border-color: rgba(124, 58, 46, 0.2) !important; color: var(--text) !important; }

  /* Tabs */
  .tabs { display: flex; gap: 0; margin-top: 0; border-bottom: 1px solid rgba(139, 100, 60, 0.15); }
  .tab-btn {
    padding: 12px 24px; border: none; background: none; color: var(--muted);
    font-size: 14px; font-weight: 600; cursor: pointer; border-bottom: 2px solid transparent;
    margin-bottom: -1px; transition: color .2s, border-color .2s;
    font-family: 'Libre Baskerville', Georgia, serif;
    letter-spacing: 0.04em;
  }
  .tab-btn:hover { color: #5c4033; }
  .tab-btn.active { color: var(--accent); border-bottom-color: var(--accent); }
  .tab-panel { display: none; }
  .tab-panel.active { display: block; }

  /* Countdown timer */
  .countdown-block {
    display: flex; align-items: center; justify-content: center; gap: 8px;
    margin-top: 24px; margin-bottom: -4px; padding: 12px 18px; border-radius: 10px;
    background: rgba(184,134,11,.07); border: 1px solid rgba(184,134,11,.18);
  }
  .countdown-icon { font-size: 18px; }
  .countdown-text {
    font-size: 14px; color: #7a5c0a; font-weight: 600;
    font-family: 'Libre Baskerville', Georgia, serif;
  }
  .countdown-block.expired { background: rgba(192,57,43,.06); border-color: rgba(192,57,43,.18); }
  .countdown-block.expired .countdown-text { color: #922b21; }
  .countdown-block.complete { background: rgba(46,125,50,.06); border-color: rgba(46,125,50,.18); }
  .countdown-block.complete .countdown-icon { color: #2e7d32; }
  .countdown-block.complete .countdown-text { color: #2e7d32; }

  /* Name fields */
  .name-block {
    margin-top: 28px; padding: 22px 24px; border-radius: 14px;
    background: var(--panel); border: 1px solid var(--border);
    box-shadow: 0 1px 4px rgba(44, 24, 16, 0.03);
  }
  .name-field label {
    display: block; font-size: 12px; color: var(--muted); margin-bottom: 7px;
    font-family: 'Libre Baskerville', Georgia, serif;
    text-transform: uppercase; letter-spacing: 0.06em;
  }
  .required-star { color: #c0392b; margin-left: 2px; }
  .name-field input {
    width: 100%; padding: 11px 14px; border-radius: 8px;
    border: 1px solid rgba(139, 100, 60, 0.18); background: #faf8f4;
    color: var(--text); font-size: 15px; outline: none; box-sizing: border-box;
    transition: border-color .2s, box-shadow .2s;
  }
  .name-field input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(124, 58, 46, 0.06); }
  .name-error {
    display: none; color: #c0392b; font-size: 13px; margin-top: 10px;
    text-align: center; font-family: 'Libre Baskerville', Georgia, serif; font-style: italic;
  }

  /* Book list */
  .book-list { list-style: none; padding: 0; margin: 20px 0 0; display: flex; flex-direction: column; gap: 10px; }
  .book-item {
    display: flex; align-items: center; gap: 14px; flex-wrap: wrap;
    background: var(--panel); border: 1px solid var(--border);
    border-radius: 14px; padding: 16px 18px;
    transition: border-color .2s, background .2s, box-shadow .2s, transform .15s;
    cursor: default;
  }
  .book-item:hover { box-shadow: 0 3px 14px rgba(44, 24, 16, 0.06); transform: translateY(-1px); }
  .book-item.rank-1 { border-color: #b8860b; background: rgba(184,134,11,.06); box-shadow: 0 3px 16px rgba(184,134,11,.1); }
  .book-item.rank-2 { border-color: #8b8682; background: rgba(139,134,130,.05); }
  .book-item.rank-3 { border-color: #a0522d; background: rgba(160,82,45,.05); }
  .book-item.rank-4 { border-color: #5b6abf; background: rgba(91,106,191,.05); }
  .book-item.vetoed  { border-color: #c0392b; background: rgba(192,57,43,.04); opacity: .5; }

  /* Book number badge */
  .book-badge {
    min-width: 40px; height: 40px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-weight: 300; font-size: 19px;
    background: linear-gradient(145deg, rgba(139, 100, 60, 0.08), rgba(139, 100, 60, 0.03));
    color: #9a7a5a; flex-shrink: 0;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-style: normal;
    border: 1px solid rgba(139, 100, 60, 0.10);
    transition: all .2s;
  }
  .book-badge.ranked-badge {
    font-style: normal; font-size: 12px; font-weight: 700;
    font-family: 'Libre Baskerville', Georgia, serif;
    letter-spacing: 0.02em;
    border-color: transparent;
  }
  .book-item.rank-1 .book-badge { background: linear-gradient(145deg, rgba(184,134,11,.18), rgba(184,134,11,.08)); color: #7a5c00; border-color: rgba(184,134,11,.2); }
  .book-item.rank-2 .book-badge { background: linear-gradient(145deg, rgba(139,134,130,.15), rgba(139,134,130,.06)); color: #5c5855; border-color: rgba(139,134,130,.18); }
  .book-item.rank-3 .book-badge { background: linear-gradient(145deg, rgba(160,82,45,.15), rgba(160,82,45,.06)); color: #8b4513; border-color: rgba(160,82,45,.18); }
  .book-item.rank-4 .book-badge { background: linear-gradient(145deg, rgba(91,106,191,.14), rgba(91,106,191,.05)); color: #4a5499; border-color: rgba(91,106,191,.18); }
  .book-item.vetoed .book-badge  { background: linear-gradient(145deg, rgba(192,57,43,.14), rgba(192,57,43,.05)); color: #a32e22; border-color: rgba(192,57,43,.18); font-style: normal; }

  .book-info { flex: 1; min-width: 0; }
  .book-title { font-weight: 600; font-size: 15px; color: var(--text); font-family: 'Libre Baskerville', Georgia, serif; line-height: 1.35; }
  .book-author { font-size: 13px; color: var(--muted); margin-top: 3px; font-style: italic; }
  .book-desc {
    font-size: 12.5px; color: #6b5744; margin-top: 6px; line-height: 1.55;
    max-height: 0; overflow: hidden; transition: max-height .3s ease;
  }
  .book-desc.open { max-height: 160px; }
  .book-link {
    display: inline-block; margin-top: 5px; font-size: 11px; color: var(--accent);
    text-decoration: none; font-weight: 600;
  }
  .book-link:hover { text-decoration: underline; }
  .book-pages {
    display: inline-block; margin-top: 5px; font-size: 11px; color: var(--muted);
    font-style: italic; margin-right: 6px;
  }
  .book-info-btn {
    background: none; border: 1px solid rgba(139, 100, 60, 0.15); border-radius: 50%;
    width: 26px; height: 26px; color: var(--muted); font-size: 12px; font-weight: 700;
    cursor: pointer; flex-shrink: 0; display: flex; align-items: center; justify-content: center;
    transition: all .2s; line-height: 1;
    font-family: 'Libre Baskerville', Georgia, serif;
  }
  .book-info-btn:hover { border-color: var(--accent); color: var(--accent); background: rgba(124, 58, 46, 0.04); }
  .book-actions { display: flex; gap: 6px; flex-shrink: 0; }
  .book-actions button {
    padding: 6px 11px; border-radius: 8px; border: 1px solid var(--border);
    background: transparent; color: var(--muted); font-size: 11px; font-weight: 600;
    cursor: pointer; transition: all .2s;
  }
  .book-actions button:hover { border-color: var(--accent); color: var(--accent); background: rgba(124, 58, 46, 0.04); }
  .book-actions button.active-rank { border-color: var(--accent); color: #fff; background: var(--accent); box-shadow: 0 2px 8px rgba(124, 58, 46, 0.2); }
  .book-actions button.active-veto { border-color: #c0392b; color: #fff; background: #c0392b; box-shadow: 0 2px 8px rgba(192, 57, 43, 0.2); }

  /* Mobile layout */
  @media (max-width: 600px) {
    .vote-subtitle { font-size: 0.95rem; }
    .name-block { padding: 18px 16px; }
    .book-item { padding: 12px 12px; gap: 8px; flex-wrap: wrap; align-items: flex-start; }
    .book-badge { min-width: 34px; height: 34px; font-size: 16px; }
    .book-badge.ranked-badge { font-size: 11px; }
    .book-info { min-width: 0; flex: 1 1 170px; }
    .book-info-btn { margin-top: 2px; }
    .book-actions { flex: 1 0 100%; gap: 4px; flex-wrap: nowrap; margin-top: 2px; }
    .book-actions button { padding: 5px 7px; font-size: 10px; border-radius: 6px; }
    .top-two { grid-template-columns: 1fr; }
    .top-card .top-book { font-size: 16px; }
    .ballot-table { font-size: 11px; }
    .ballot-table th, .ballot-table td { padding: 4px 4px; }
    .round-row { font-size: 12px; }
    .round-row .round-votes { gap: 6px; }
    .round-vote-segment.third, .round-vote-segment.fourth { display: none; }
    .dl-row { flex-direction: column; }
    .dl-row button { width: 100%; }
    .card-carousel-wrap { min-height: 140px; margin-top: 14px; }
    .carousel-card { padding: 20px 16px; }
    .carousel-card .card-text { font-size: 14px; line-height: 1.55; margin-bottom: 10px; }
    .carousel-card .card-author { font-size: 10px; }
    .carousel-nav button { width: 30px; height: 30px; font-size: 14px; }
    .add-card-wrap { margin-top: 12px; }
    .add-card-form textarea { font-size: 13px; min-height: 56px; padding: 10px 12px; }
    .add-card-prompt { font-size: 12px; }
    .add-card-actions button { padding: 7px 14px; font-size: 12px; }
    .rabbit-gif { width: 44px; height: 40px; }
  }

  /* Ballot summary */
  .vote-summary {
    margin-top: 32px; padding: 24px; border-radius: 14px;
    background: var(--panel); border: 1px solid var(--border);
    box-shadow: 0 1px 4px rgba(44, 24, 16, 0.03);
  }
  .vote-summary h3 {
    margin: 0 0 16px; font-size: 16px; color: var(--accent);
    font-family: 'Libre Baskerville', Georgia, serif;
    letter-spacing: 0.02em;
  }
  .vote-summary .slot { display: flex; gap: 10px; align-items: center; margin: 8px 0; font-size: 14px; }
  .vote-summary .slot-label {
    color: var(--muted); min-width: 85px;
    font-family: 'Libre Baskerville', Georgia, serif; font-size: 13px;
  }
  .vote-summary .slot-value { color: var(--text); font-weight: 500; }
  .vote-submit {
    margin-top: 22px; width: 100%; padding: 14px; border-radius: 10px;
    background: var(--accent); color: #faf7f2; font-weight: 700; font-size: 15px;
    border: none; cursor: pointer; transition: all .25s;
    font-family: 'Libre Baskerville', Georgia, serif; letter-spacing: 0.03em;
    box-shadow: 0 2px 8px rgba(124, 58, 46, 0.15);
  }
  .vote-submit.not-ready { opacity: .35; cursor: default; box-shadow: none; }
  .vote-submit:not(:disabled):hover { opacity: .9; box-shadow: 0 4px 18px rgba(124, 58, 46, 0.25); transform: translateY(-1px); }
  .vote-toast {
    margin-top: 14px; padding: 12px 16px; border-radius: 10px;
    background: rgba(124, 58, 46, 0.06); color: var(--accent);
    font-size: 13px; display: none; text-align: center;
    border: 1px solid rgba(124, 58, 46, 0.1);
  }

  /* Results tab */
  .results-list { list-style: none; padding: 0; margin: 24px 0 0; display: flex; flex-direction: column; gap: 8px; }
  .result-item {
    display: flex; align-items: center; gap: 14px;
    background: var(--panel); border: 1px solid var(--border);
    border-radius: 14px; padding: 16px 20px;
  }
  .result-rank {
    min-width: 30px; height: 30px; border-radius: 50%; display: flex;
    align-items: center; justify-content: center; font-weight: 700; font-size: 13px;
    background: var(--accent-soft); color: var(--accent); flex-shrink: 0;
    font-family: 'Libre Baskerville', Georgia, serif;
  }
  .result-rank.r1 { background: linear-gradient(145deg, rgba(184,134,11,.18), rgba(184,134,11,.08)); color: #7a5c00; }
  .result-rank.r2 { background: linear-gradient(145deg, rgba(139,134,130,.15), rgba(139,134,130,.06)); color: #5c5855; }
  .result-rank.r3 { background: linear-gradient(145deg, rgba(160,82,45,.15), rgba(160,82,45,.06)); color: #8b4513; }
  .result-book { flex: 1; font-weight: 600; font-size: 15px; font-family: 'Libre Baskerville', Georgia, serif; }
  .result-score { font-size: 13px; color: var(--muted); }
  .result-bar-wrap { width: 100px; height: 6px; background: var(--border); border-radius: 3px; overflow: hidden; }
  .result-bar { height: 100%; background: var(--accent); border-radius: 3px; transition: width .4s; }
  .results-empty {
    color: var(--muted); font-size: 15px; margin-top: 24px; text-align: center; padding: 40px;
    font-family: 'Libre Baskerville', Georgia, serif; font-style: italic;
  }
  .results-refresh {
    margin-top: 16px; padding: 8px 18px; border-radius: 8px;
    border: 1px solid var(--border); background: transparent; color: var(--muted);
    font-size: 13px; font-weight: 600; cursor: pointer; transition: all .2s;
  }
  .results-refresh:hover { border-color: var(--accent); color: var(--accent); }
  .results-header { display: flex; align-items: center; justify-content: space-between; margin-top: 28px; gap: 14px; }
  .results-header span { font-size: 13px; color: var(--muted); font-style: italic; min-width: 0; }
  .results-refresh { flex-shrink: 0; }
  .results-section-title {
    font-size: 12px; color: var(--muted); margin: 28px 0 10px;
    text-transform: uppercase; letter-spacing: .08em;
    font-family: 'Libre Baskerville', Georgia, serif;
  }
  .result-item.winner { border-color: #b8860b; background: rgba(184,134,11,.05); }
  .result-item.winner .result-rank { background: linear-gradient(145deg, rgba(184,134,11,.22), rgba(184,134,11,.1)); color: #7a5c00; }
  .result-item.eliminated { opacity: .5; }
  .result-item.vetoed-item { opacity: .4; border-color: #c0392b; }
  .result-item.vetoed-item .result-rank { background: rgba(192,57,43,.1); color: #c0392b; }
  .round-block {
    margin-top: 14px; padding: 16px 18px; border-radius: 12px;
    background: var(--panel); border: 1px solid var(--border);
  }
  .round-title {
    font-size: 13px; color: var(--accent); font-weight: 600; margin-bottom: 10px;
    font-family: 'Libre Baskerville', Georgia, serif;
  }
  .round-row { display: flex; align-items: center; gap: 10px; padding: 5px 0; font-size: 13px; }
  .round-row .round-name { flex: 1; color: var(--text); }
  .round-row .round-votes {
    color: var(--muted); min-width: 50px; text-align: right;
    display: flex; justify-content: flex-end; gap: 8px; flex-wrap: wrap;
  }
  .round-vote-segment { white-space: nowrap; }
  .round-vote-segment.first { font-weight: 700; color: var(--text); }
  .round-vote-segment + .round-vote-segment::before { content: " | "; }
  .round-row.elim { color: #c0392b; opacity: .65; text-decoration: line-through; }
  .round-row.win { color: #7a5c00; font-weight: 600; }
  .round-reason { font-size: 12px; color: var(--muted); margin-top: 5px; font-style: italic; line-height: 1.5; }

  /* Top 2 hero */
  .top-two { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 28px; }
  .top-card {
    padding: 24px 20px; border-radius: 14px; text-align: center;
    border: 1px solid var(--border); background: var(--panel);
    transition: transform .2s;
  }
  .top-card:hover { transform: translateY(-2px); }
  .top-card.gold   { border-color: #b8860b; background: rgba(184,134,11,.05); box-shadow: 0 4px 18px rgba(184,134,11,.08); }
  .top-card.silver { border-color: #8b8682; background: rgba(139,134,130,.04); }
  .top-card.bronze { border-color: #a0522d; background: rgba(160,82,45,.04); }
  .top-card .top-label {
    font-size: 10px; text-transform: uppercase; letter-spacing: .12em; margin-bottom: 8px;
    font-family: 'Libre Baskerville', Georgia, serif;
  }
  .top-card.gold .top-label   { color: #8b6914; }
  .top-card.silver .top-label { color: #6b6560; }
  .top-card.bronze .top-label { color: #7a3e1e; }
  .top-card .top-book { font-size: 20px; font-weight: 600; color: var(--text); font-family: 'Cormorant Garamond', Georgia, serif; line-height: 1.3; }
  .top-card .top-votes { font-size: 13px; color: var(--muted); margin-top: 6px; font-style: italic; }

  /* Download data */
  /* Voting in progress banner */
  .voting-progress-banner {
    display: flex; align-items: center; gap: 10px;
    padding: 12px 18px; border-radius: 10px; margin-bottom: 16px;
    background: rgba(184,134,11,.07); border: 1px solid rgba(184,134,11,.22);
  }
  .voting-progress-dot {
    width: 8px; height: 8px; border-radius: 50%; background: #b8860b; flex-shrink: 0;
    animation: pulse-dot 1.6s ease-in-out infinite;
  }
  @keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: .4; transform: scale(.75); }
  }
  .voting-progress-text {
    font-size: 13px; color: #7a5c0a;
    font-family: 'Libre Baskerville', Georgia, serif;
  }
  /* Awaiting votes section */
  .awaiting-block {
    margin-top: 16px; padding: 16px 20px; border-radius: 12px;
    background: rgba(139, 100, 60, 0.04); border: 1px solid rgba(139, 100, 60, 0.12);
  }
  .awaiting-label {
    font-size: 11px; text-transform: uppercase; letter-spacing: 0.08em;
    color: var(--muted); font-family: 'Libre Baskerville', Georgia, serif;
    margin-bottom: 8px;
  }
  .awaiting-names {
    font-size: 14px; color: #6b5344;
    font-family: 'Libre Baskerville', Georgia, serif;
    font-style: italic; line-height: 1.7;
  }

  .dl-block {
    margin-top: 32px; padding: 22px 24px; border-radius: 14px;
    background: var(--panel); border: 1px solid var(--border);
  }
  .dl-block h3 {
    margin: 0 0 12px; font-size: 14px; color: var(--accent);
    font-family: 'Libre Baskerville', Georgia, serif;
  }
  .dl-row { display: flex; gap: 8px; align-items: center; }
  .dl-row input {
    flex: 1; padding: 10px 14px; border-radius: 8px;
    border: 1px solid var(--border); background: #faf8f4;
    color: var(--text); font-size: 14px; outline: none;
    transition: border-color .2s, box-shadow .2s;
  }
  .dl-row input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(124, 58, 46, 0.06); }
  .dl-row button {
    padding: 10px 18px; border-radius: 8px; border: 1px solid var(--accent);
    background: var(--accent-soft); color: var(--accent);
    font-size: 13px; font-weight: 600; cursor: pointer; white-space: nowrap;
    transition: all .2s;
  }
  .dl-row button:hover { background: var(--accent); color: #fff; }
  .dl-error { font-size: 12px; color: #c0392b; margin-top: 8px; display: none; }
  .ballot-table { width: 100%; border-collapse: collapse; margin-top: 16px; font-size: 13px; display: none; }
  .ballot-table th {
    text-align: left; color: var(--muted); border-bottom: 1px solid rgba(139,100,60,.15);
    padding: 8px 8px; font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: .04em;
  }
  .ballot-table td { padding: 8px 8px; color: var(--text); border-bottom: 1px solid rgba(139,100,60,.06); }
  .ballot-table td.veto-cell { color: #c0392b; }
  .ballot-delete-btn {
    background: none; border: none; cursor: pointer; color: rgba(192,57,43,0.4);
    font-size: 15px; line-height: 1; padding: 2px 4px; border-radius: 4px;
    transition: color .15s, background .15s;
  }
  .ballot-delete-btn:hover { color: #c0392b; background: rgba(192,57,43,0.08); }

  /* Waiting-room card carousel */
  .card-carousel-wrap {
    margin-top: 20px; position: relative; min-height: 180px;
    display: flex; flex-direction: column; align-items: center;
  }
  .card-carousel-cta {
    font-family: 'Libre Baskerville', Georgia, serif;
    font-size: 13px; color: var(--muted); text-align: center;
    cursor: pointer; padding: 10px 22px; border-radius: 10px;
    border: 1px dashed rgba(139,100,60,.25); background: rgba(139,100,60,.03);
    transition: border-color .2s, background .2s;
  }
  .card-carousel-cta:hover { border-color: var(--accent); background: rgba(124,58,46,.05); }
  .card-stage {
    width: 100%; max-width: 440px; perspective: 800px;
    display: flex; justify-content: center; align-items: flex-start;
    position: relative; margin: 0 auto;
  }
  .carousel-card {
    width: 100%; padding: 28px 24px; border-radius: 14px; text-align: center;
    border: 1px solid var(--border); background: var(--panel);
    box-shadow: 0 4px 20px rgba(80,50,30,.06);
    font-family: 'Libre Baskerville', Georgia, serif;
    animation: cardFadeIn .45s ease;
    position: relative;
  }
  .card-delete-btn {
    position: absolute; top: 8px; right: 8px;
    background: none; border: none; cursor: pointer;
    font-size: 18px; color: var(--muted); line-height: 1;
    padding: 2px 6px; border-radius: 4px; opacity: 0.4;
    transition: opacity .15s, color .15s;
  }
  .card-delete-btn:hover { opacity: 1; color: #c0392b; }
  .carousel-card .card-text {
    font-size: 16px; line-height: 1.65; color: var(--text);
    font-style: italic; margin-bottom: 12px;
  }
  .carousel-card .card-author {
    font-size: 12px; color: var(--muted); text-transform: uppercase;
    letter-spacing: .08em;
  }
  @keyframes cardFadeIn { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
  .carousel-nav {
    display: flex; gap: 12px; margin-top: 14px; align-items: center; justify-content: center;
    width: 100%;
  }
  .carousel-nav button {
    background: none; border: 1px solid var(--border); border-radius: 50%;
    width: 34px; height: 34px; cursor: pointer; font-size: 16px; color: var(--muted);
    display: flex; align-items: center; justify-content: center;
    transition: border-color .2s, color .2s;
  }
  .carousel-nav button:hover { border-color: var(--accent); color: var(--accent); }
  .carousel-dots {
    font-family: 'Libre Baskerville', Georgia, serif;
    font-size: 12px; color: var(--muted); letter-spacing: .04em;
    min-width: 40px; text-align: center;
  }
  .rabbit-gif {
    width: 56px; height: 52px; margin: 4px auto 0; display: block;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 72'%3E%3Cellipse cx='22' cy='14' rx='3.5' ry='14' fill='%237c3a2e' transform='rotate(-10,22,14)'/%3E%3Cellipse cx='22' cy='14' rx='1.8' ry='10' fill='%23a0584a' transform='rotate(-10,22,14)'/%3E%3Cellipse cx='36' cy='12' rx='3.2' ry='14.5' fill='%237c3a2e' transform='rotate(6,36,12)'/%3E%3Cellipse cx='36' cy='12' rx='1.6' ry='10.5' fill='%23a0584a' transform='rotate(6,36,12)'/%3E%3Cellipse cx='30' cy='32' rx='13' ry='11.5' fill='%237c3a2e'/%3E%3Ccircle cx='35' cy='30' r='2.2' fill='%23f5ede0'/%3E%3Ccircle cx='35.5' cy='29.8' r='.8' fill='%232c1810'/%3E%3Cellipse cx='40' cy='33' rx='1.5' ry='1' fill='%23a04a3a'/%3E%3Cellipse cx='26' cy='52' rx='17' ry='14' fill='%237c3a2e'/%3E%3Ccircle cx='9' cy='47' r='5' fill='%23f5ede0' opacity='.85'/%3E%3Cellipse cx='36' cy='65' rx='5.5' ry='3.5' fill='%237c3a2e'/%3E%3Cellipse cx='14' cy='65' rx='9' ry='3.5' fill='%237c3a2e' transform='rotate(-10,14,65)'/%3E%3C/svg%3E");
    background-size: contain; background-repeat: no-repeat; background-position: center;
    opacity: 0;
  }
  .rabbit-gif.hopping { animation: rabbitHop 1.2s cubic-bezier(.22,.61,.36,1) forwards; }
  @keyframes rabbitHop {
    0%   { opacity: 0; transform: translateX(-20px) translateY(0) rotate(0deg); }
    8%   { opacity: 1; transform: translateX(-12px) translateY(0) rotate(0deg); }
    18%  { transform: translateX(-2px) translateY(-13px) rotate(-3deg); }
    28%  { transform: translateX(8px) translateY(-1px) rotate(1deg); }
    40%  { transform: translateX(18px) translateY(-14px) rotate(-3deg); }
    52%  { transform: translateX(30px) translateY(-1px) rotate(1deg); }
    64%  { transform: translateX(40px) translateY(-12px) rotate(-2deg); }
    76%  { opacity: 1; transform: translateX(48px) translateY(0) rotate(0deg); }
    90%  { opacity: .3; transform: translateX(55px) translateY(0) rotate(0deg); }
    100% { opacity: 0; transform: translateX(60px) translateY(0) rotate(0deg); }
  }

  /* Add-card form */
  .add-card-wrap {
    margin-top: 18px; width: 100%; max-width: 440px;
    text-align: center;
  }
  .add-card-btn {
    font-family: 'Libre Baskerville', Georgia, serif;
    font-size: 12px; color: var(--accent); cursor: pointer;
    background: none; border: none; text-decoration: underline;
    text-underline-offset: 3px;
  }
  .add-card-form {
    display: none; margin-top: 12px; text-align: left;
  }
  .add-card-form.open { display: block; }
  .add-card-prompt {
    font-family: 'Libre Baskerville', Georgia, serif;
    font-size: 13px; color: var(--muted); font-style: italic;
    margin-bottom: 10px; line-height: 1.6;
  }
  .add-card-form textarea {
    width: 100%; min-height: 68px; padding: 12px 14px; border-radius: 10px; box-sizing: border-box;
    border: 1px solid var(--border); background: #faf8f4; color: var(--text);
    font-size: 14px; font-family: 'Libre Baskerville', Georgia, serif;
    resize: vertical; outline: none; transition: border-color .2s;
  }
  .add-card-form textarea:focus { border-color: var(--accent); }
  .add-card-form .char-count {
    font-size: 11px; color: var(--muted); text-align: right; margin-top: 4px;
  }
  .add-card-actions { display: flex; gap: 8px; margin-top: 10px; justify-content: flex-end; }
  .add-card-actions button {
    padding: 8px 18px; border-radius: 8px; font-size: 13px; cursor: pointer;
    font-family: 'Libre Baskerville', Georgia, serif; border: 1px solid var(--border);
    transition: all .2s;
  }
  .add-card-cancel { background: transparent; color: var(--muted); }
  .add-card-submit { background: var(--accent-soft); color: var(--accent); border-color: var(--accent) !important; font-weight: 600; }
  .add-card-submit:hover { background: var(--accent); color: #fff; }

  /* Admin tab */
  .tab-admin-btn { margin-left: auto; }
  .admin-book-btn { border-color: rgba(124,58,46,.35) !important; }
  .admin-book-btn.admin-del { color: #c0392b !important; border-color: rgba(192,57,43,.35) !important; }
  .admin-book-btn.admin-approve { color: #2e7d32 !important; border-color: rgba(46,125,50,.4) !important; }
  .admin-bar {
    display: flex; align-items: center; justify-content: space-between;
    margin-top: 24px; padding: 12px 16px; border-radius: 10px;
    background: rgba(124,58,46,.06); border: 1px solid rgba(124,58,46,.15);
  }
  .admin-bar-label {
    font-family: 'Libre Baskerville', Georgia, serif; font-size: 13px;
    font-weight: 700; color: var(--accent); letter-spacing: .04em;
  }
  .admin-section {
    margin-top: 22px; padding: 20px; border-radius: 14px;
    background: var(--panel); border: 1px solid var(--border);
  }
  .admin-h3 {
    margin: 0 0 14px; font-size: 15px; color: var(--accent);
    font-family: 'Libre Baskerville', Georgia, serif; letter-spacing: .02em;
  }
  .admin-toggle-row {
    display: flex; align-items: center; justify-content: space-between;
    padding: 10px 0; border-bottom: 1px solid rgba(139,100,60,.08);
  }
  .admin-toggle-row:last-child { border-bottom: none; }
  .admin-toggle-name { font-weight: 600; font-size: 14px; color: var(--text); }
  .admin-toggle-sub { font-size: 12.5px; margin-top: 2px; font-style: italic; }
  .admin-toggle-sub.open { color: #2e7d32; }
  .admin-toggle-sub.closed { color: #c0392b; }
  .pill-toggle {
    padding: 8px 16px; border-radius: 999px; border: 1px solid var(--accent);
    background: var(--accent-soft); color: var(--accent); font-size: 13px;
    font-weight: 600; cursor: pointer; transition: all .2s; white-space: nowrap;
  }
  .pill-toggle:hover { background: var(--accent); color: #fff; }
  .admin-danger { border-color: rgba(192,57,43,.25); }
  .admin-danger-btns { display: flex; gap: 10px; flex-wrap: wrap; }
  .admin-hist-row {
    display: flex; align-items: center; gap: 10px; padding: 10px 0;
    border-bottom: 1px solid rgba(139,100,60,.08); flex-wrap: wrap;
  }
  .admin-hist-row:last-child { border-bottom: none; }
  .admin-hist-name { flex: 1; min-width: 0; font-size: 14px; color: var(--text); }
  .admin-hist-name span { color: var(--muted); font-size: 12.5px; font-style: italic; }
  .book-form {
    margin-top: 12px; padding: 18px; border-radius: 14px; text-align: left;
    background: var(--panel); border: 1px solid var(--border);
    display: flex; flex-direction: column; gap: 10px;
  }
  .book-form input {
    padding: 10px 14px; border-radius: 8px; border: 1px solid rgba(139,100,60,.18);
    background: #faf8f4; color: var(--text); font-size: 14px; outline: none;
  }
  .book-form input:focus, .sg-textarea:focus, .book-form textarea:focus { border-color: var(--accent); }
  .sg-textarea, .book-form textarea {
    width: 100%; min-height: 64px; padding: 11px 14px; border-radius: 8px; box-sizing: border-box;
    border: 1px solid rgba(139,100,60,.18); background: #faf8f4; color: var(--text);
    font-size: 14px; font-family: inherit; resize: vertical; outline: none;
  }
  .reset-note { font-size: 13px; color: var(--muted); line-height: 1.6; margin: 0 0 12px; }
  .reset-btn {
    padding: 10px 18px; border-radius: 8px; border: 1px solid #c0392b;
    background: rgba(192,57,43,.06); color: #c0392b; font-weight: 600;
    font-size: 13px; cursor: pointer; transition: all .2s;
  }
  .reset-btn:hover { background: #c0392b; color: #fff; }

  /* Curation notice (ballot too small / round not open yet) */
  .curation-notice {
    margin-top: 28px; padding: 36px 24px; border-radius: 14px; text-align: center;
    background: var(--panel); border: 1px dashed rgba(139,100,60,.3);
  }
  .curation-title {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 26px; color: var(--accent); margin-bottom: 8px;
  }
  .curation-notice p { font-size: 14px; color: var(--muted); font-style: italic; margin: 0 0 16px; }

  /* Suggest tab */
  .name-field + .name-field { margin-top: 14px; }
  .suggest-intro {
    font-family: 'Libre Baskerville', Georgia, serif; font-style: italic;
    font-size: 13px; color: var(--muted); line-height: 1.7; margin: 24px 4px 0;
    text-align: center;
  }

  /* History tab */
  .history-winner {
    font-size: 14px; color: var(--text); margin: 6px 0 10px;
    font-family: 'Libre Baskerville', Georgia, serif;
  }
  .history-detail { margin-top: 12px; }
</style>

<div class="vote-content-area">
<!-- Tabs -->
<div class="tabs">
  <button class="tab-btn active" data-tab="vote">Vote</button>
  <button class="tab-btn" data-tab="suggest">Suggest</button>
  <button class="tab-btn" data-tab="results">Results</button>
  <button class="tab-btn" data-tab="history">History</button>
  <button class="tab-btn tab-admin-btn" data-tab="admin">Admin</button>
</div>

<!-- Vote tab -->
<div class="tab-panel active" id="tab-vote">
  <div class="countdown-block complete" id="countdownBlock">
    <span class="countdown-icon">&#10003;</span>
    <span class="countdown-text" id="countdownText">Voting Complete. See results!</span>
  </div>
  <div class="curation-notice" id="curationNotice" style="display:none">
    <div class="curation-title">The next round is being curated</div>
    <p>Not enough books on the ballot yet &mdash; voting opens once there are at least five.</p>
    <button class="results-refresh" id="curationSuggestBtn">Suggest a book &#8594;</button>
  </div>
  <div class="curation-notice" id="votingClosedNotice" style="display:none">
    <div class="curation-title">Voting is closed</div>
    <p>The admin has closed voting for now. Check the Results tab to see how it turned out.</p>
  </div>
  <div class="name-block">
    <div class="name-field">
      <label for="displayName">Name <span class="required-star">*</span></label>
      <input type="text" id="displayName" placeholder="e.g. Flamen Ball" autocomplete="name">
    </div>
  </div>

  <ul class="book-list" id="bookList"></ul>

  <div class="vote-summary">
    <h3>Your Ballot</h3>
    <div class="slot"><span class="slot-label">1st choice</span><span class="slot-value" id="slot1">—</span></div>
    <div class="slot"><span class="slot-label">2nd choice</span><span class="slot-value" id="slot2">—</span></div>
    <div class="slot"><span class="slot-label">3rd choice</span><span class="slot-value" id="slot3">—</span></div>
    <div class="slot"><span class="slot-label">4th choice</span><span class="slot-value" id="slot4">—</span></div>
    <div class="slot"><span class="slot-label">Veto</span><span class="slot-value" id="slotVeto">None</span></div>
    <button class="vote-submit not-ready" id="submitBtn">Submit Vote</button>
    <div class="name-error" id="nameError"></div>
    <div class="vote-toast" id="toast"></div>
  </div>
</div>

<!-- Results tab -->
<div class="tab-panel" id="tab-results">
  <div class="results-header">
    <span id="resultsSubtitle">Loading...</span>
    <button class="results-refresh" id="refreshBtn">Refresh</button>
  </div>
  <div id="topTwo"></div>
  <div id="cardCarousel"></div>
  <ul class="results-list" id="resultsList"></ul>
</div>

<!-- Suggest tab -->
<div class="tab-panel" id="tab-suggest">
  <p class="suggest-intro">Have a book the club should read? Suggest it here &mdash; suggestions appear below and join the ballot once approved.</p>
  <div class="curation-notice" id="suggestClosedNotice" style="display:none">
    <div class="curation-title">Suggestions are closed</div>
    <p>The admin isn&rsquo;t taking new book suggestions right now.</p>
  </div>
  <div class="name-block" id="suggestFormBlock">
    <div class="name-field">
      <label for="sgTitle">Book Title <span class="required-star">*</span></label>
      <input type="text" id="sgTitle" placeholder="e.g. The Overstory">
    </div>
    <div class="name-field">
      <label for="sgAuthor">Author <span class="required-star">*</span></label>
      <input type="text" id="sgAuthor" placeholder="e.g. Richard Powers">
    </div>
    <div class="name-field">
      <label for="sgUrl">Link (optional)</label>
      <input type="text" id="sgUrl" placeholder="Goodreads, publisher...">
    </div>
    <div class="name-field">
      <label for="sgNote">Why this book? (optional)</label>
      <textarea class="sg-textarea" id="sgNote" placeholder="Make your case..."></textarea>
    </div>
    <div class="name-field">
      <label for="sgName">Your name</label>
      <input type="text" id="sgName" autocomplete="name">
    </div>
    <button class="vote-submit" id="sgSubmit" style="margin-top:18px">Suggest Book</button>
    <div class="vote-toast" id="sgToast"></div>
  </div>
  <div class="results-section-title">Awaiting approval</div>
  <ul class="book-list" id="suggestionList"></ul>
  <div class="results-empty" id="suggestionEmpty" style="display:none">No suggestions yet. Be the first!</div>
</div>

<!-- History tab -->
<div class="tab-panel" id="tab-history">
  <div id="historyList"></div>
  <div class="results-empty" id="historyEmpty" style="display:none">No past votes yet &mdash; history appears once a round is closed.</div>
</div>

<!-- Admin tab -->
<div class="tab-panel" id="tab-admin">
  <!-- Locked: password gate -->
  <div class="name-block" id="adminGate">
    <div class="name-field">
      <label for="adminPw">Admin password</label>
      <input type="password" id="adminPw" placeholder="Enter to unlock controls" autocomplete="current-password">
    </div>
    <button class="vote-submit" id="adminUnlockBtn" style="margin-top:16px">Unlock</button>
    <div class="name-error" id="adminGateError"></div>
  </div>

  <!-- Unlocked: dashboard -->
  <div id="adminDashboard" style="display:none">
    <div class="admin-bar">
      <span class="admin-bar-label">Admin mode</span>
      <button class="results-refresh" id="adminLockBtn">Lock</button>
    </div>

    <div class="admin-section">
      <h3 class="admin-h3">Status</h3>
      <div class="admin-toggle-row">
        <div><div class="admin-toggle-name">Voting</div><div class="admin-toggle-sub" id="votingStateLabel">&mdash;</div></div>
        <button class="pill-toggle" id="votingToggle">Toggle</button>
      </div>
      <div class="admin-toggle-row">
        <div><div class="admin-toggle-name">Suggestions</div><div class="admin-toggle-sub" id="suggestStateLabel">&mdash;</div></div>
        <button class="pill-toggle" id="suggestToggle">Toggle</button>
      </div>
    </div>

    <div class="admin-section">
      <h3 class="admin-h3">Books on the ballot</h3>
      <ul class="book-list" id="adminBookList"></ul>
      <button class="results-refresh" id="addBookBtn" style="margin-top:12px">+ Add book</button>
      <div class="book-form" id="bookForm" style="display:none">
        <input id="bfTitle" placeholder="Title *">
        <input id="bfAuthor" placeholder="Author *">
        <input id="bfPages" type="number" placeholder="Pages">
        <input id="bfUrl" placeholder="Link (Goodreads etc.)">
        <textarea id="bfDesc" placeholder="Short description"></textarea>
        <div class="add-card-actions">
          <button class="add-card-cancel" id="bfCancel">Cancel</button>
          <button class="add-card-submit" id="bfSave">Save Book</button>
        </div>
        <div class="dl-error" id="bfError"></div>
      </div>
    </div>

    <div class="admin-section">
      <h3 class="admin-h3">Pending suggestions</h3>
      <ul class="book-list" id="adminSuggestionList"></ul>
      <div class="results-empty" id="adminSuggestionEmpty" style="display:none">No pending suggestions.</div>
    </div>

    <div class="admin-section">
      <h3 class="admin-h3">Votes cast</h3>
      <table class="ballot-table" id="adminBallotTable" style="display:none">
        <thead><tr><th>Voter</th><th>1st</th><th>2nd</th><th>3rd</th><th>4th</th><th>Veto</th><th></th></tr></thead>
        <tbody id="adminBallotBody"></tbody>
      </table>
      <div class="results-empty" id="adminBallotEmpty" style="display:none">No votes yet.</div>
    </div>

    <div class="admin-section">
      <h3 class="admin-h3">History</h3>
      <div id="adminHistoryList"></div>
      <div class="results-empty" id="adminHistoryEmpty" style="display:none">No archived rounds.</div>
    </div>

    <div class="admin-section admin-danger">
      <h3 class="admin-h3">End this round</h3>
      <p class="reset-note">Clears all ballots and cards and empties the book list. Pending suggestions are kept. Choose whether to save a snapshot to History first.</p>
      <div class="admin-danger-btns">
        <button class="reset-btn" id="resetArchiveBtn">Archive &amp; Reset</button>
        <button class="reset-btn" id="resetPlainBtn">Reset without archiving</button>
      </div>
      <div class="dl-error" id="resetError"></div>
    </div>
  </div>
</div>

<script>
(function(){
  // Books come from the DB (see /vote/books); admins manage them in the Admin tab.
  var BOOKS = [];
  var MIN_BOOKS = 5;  // 4 ranks + a veto need at least this many candidates

  // Site state (voting/suggestions open) — public, reflected across tabs.
  var SETTINGS = { voting_open: "1", suggestions_open: "1" };

  // Admin — unlocked with the ballot password, remembered per browser.
  var adminUnlocked = false;
  var _adminPw = "";
  try { _adminPw = localStorage.getItem("bc_admin_pw") || ""; } catch(e) {}

  function votingOpen() { return SETTINGS.voting_open === "1"; }
  function suggestionsOpen() { return SETTINGS.suggestions_open === "1"; }

  async function loadSettings() {
    try {
      const resp = await fetch("/vote/settings");
      const data = await resp.json();
      if (data && data.voting_open !== undefined) SETTINGS = data;
    } catch(e) {}
    applyGating();
  }

  // Reflect open/closed state on the Vote and Suggest tabs.
  function applyGating() {
    const votingClosed = !votingOpen();
    document.getElementById("votingClosedNotice").style.display = votingClosed ? "" : "none";
    const sgClosed = !suggestionsOpen();
    document.getElementById("suggestClosedNotice").style.display = sgClosed ? "" : "none";
    document.getElementById("suggestFormBlock").style.display = sgClosed ? "none" : "";
    render();
  }

  async function loadBooks() {
    try {
      const resp = await fetch("/vote/books");
      const data = await resp.json();
      BOOKS = data.books || [];
      // Shuffle books so order is different for each visitor
      for (let i = BOOKS.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [BOOKS[i], BOOKS[j]] = [BOOKS[j], BOOKS[i]];
      }
    } catch(e) { BOOKS = []; }
    // Indexes shift on reload, so any in-progress selections reset with them
    state.ranks = [null, null, null, null];
    state.veto = null;
    render();
    if (adminUnlocked) renderAdminBooks();
  }

  const NUM_RANKS = 4;
  const state = { ranks: [null, null, null, null], veto: null, hasSubmitted: false };
  const suffixes = ["st","nd","rd","th"];
  function suf(n) { return n + suffixes[Math.min(n-1,3)]; }
  const EXPECTED_VOTERS = ["Gloria","Sheila","Matias","Henry","Matt","Leah","Chris","Scott","Alexander"];

  // --- Tabs ---
  document.querySelectorAll(".tab-btn").forEach(btn => {
    btn.addEventListener("click", function() {
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
      this.classList.add("active");
      document.getElementById("tab-" + this.dataset.tab).classList.add("active");
      if (this.dataset.tab === "results") loadResults();
      if (this.dataset.tab === "suggest") loadSuggestions();
      if (this.dataset.tab === "history") loadHistory();
      if (this.dataset.tab === "admin") openAdminTab();
    });
  });

  // --- Vote tab ---
  function getName() { return document.getElementById("displayName").value.trim(); }

  const ORDINALS = ["1st","2nd","3rd","4th"];
  function getMissingMessage() {
    const missingName = !getName();
    const missingRanks = [];
    for (let r = 0; r < NUM_RANKS; r++) {
      if (state.ranks[r] === null) missingRanks.push(ORDINALS[r]);
    }
    if (!missingName && !missingRanks.length) return "";

    // Build parts: name comes first, then rank ordinals joined together
    const parts = [];
    if (missingName) parts.push("your name");
    if (missingRanks.length) {
      let rankStr;
      if (missingRanks.length === 1) rankStr = missingRanks[0];
      else if (missingRanks.length === 2) rankStr = missingRanks[0] + " and " + missingRanks[1];
      else rankStr = missingRanks.slice(0, -1).join(", ") + ", and " + missingRanks[missingRanks.length - 1];
      // Only append "choice" once at the end
      parts.push("your " + rankStr + " choice");
    }
    let joined;
    if (parts.length === 1) joined = parts[0].charAt(0).toUpperCase() + parts[0].slice(1);
    else joined = parts[0].charAt(0).toUpperCase() + parts[0].slice(1) + " and " + parts[1];
    return "Enter " + joined + " before submitting.";
  }

  function checkSubmit() {
    const filled = state.ranks.filter(v => v !== null).length;
    const btn = document.getElementById("submitBtn");
    const ready = filled === NUM_RANKS && getName();
    btn.classList.toggle("not-ready", !ready);
    if (ready && btn.textContent === "Submitted") btn.textContent = "Resubmit";
    // Hide error as soon as everything is filled
    if (ready) document.getElementById("nameError").style.display = "none";
  }

  function render() {
    const list = document.getElementById("bookList");
    const tooFew = BOOKS.length < MIN_BOOKS;
    const closed = !votingOpen();
    const canVote = !tooFew && !closed;

    // Vote tab visibility: closed (admin) > curation (too few) > open ballot.
    document.getElementById("votingClosedNotice").style.display = closed ? "" : "none";
    document.getElementById("curationNotice").style.display = (tooFew && !closed) ? "" : "none";
    document.getElementById("countdownBlock").style.display = canVote ? "" : "none";
    document.querySelector("#tab-vote .name-block").style.display = canVote ? "" : "none";
    document.querySelector("#tab-vote .vote-summary").style.display = canVote ? "" : "none";

    if (!canVote) { list.innerHTML = ""; return; }

    list.innerHTML = BOOKS.map((b, i) => {
      const rankIdx = state.ranks.indexOf(i);
      const isVetoed = state.veto === i;
      let cls = "book-item";
      let badge = "";
      if      (rankIdx === 0) { cls += " rank-1"; badge = "1st"; }
      else if (rankIdx === 1) { cls += " rank-2"; badge = "2nd"; }
      else if (rankIdx === 2) { cls += " rank-3"; badge = "3rd"; }
      else if (rankIdx === 3) { cls += " rank-4"; badge = "4th"; }
      else if (isVetoed)      { cls += " vetoed";  badge = "\\u2718"; }

      let btns = "";
      for (let r = 1; r <= NUM_RANKS; r++) {
        const active = state.ranks[r-1] === i ? "active-rank" : "";
        btns += '<button class="' + active + '" data-book="' + i + '" data-rank="' + r + '">' + suf(r) + '</button>';
      }
      const vetoActive = isVetoed ? "active-veto" : "";
      btns += '<button class="' + vetoActive + '" data-book="' + i + '" data-action="veto">Veto</button>';
      const badgeClass = badge ? "book-badge ranked-badge" : "book-badge";
      return '<li class="' + cls + '">'
        + '<div class="' + badgeClass + '">' + (badge || (i + 1)) + '</div>'
        + '<div class="book-info">'
        +   '<div class="book-title">' + _escHtml(b.title) + '</div>'
        +   '<div class="book-author">' + _escHtml(b.author) + '</div>'
        +   '<div class="book-desc" id="desc-' + i + '">' + _escHtml(b.desc || "")
        +     (b.pages ? ' <span class="book-pages">' + b.pages + ' pages</span>' : '')
        +     (b.url ? ' <a class="book-link" href="' + _escHtml(b.url) + '" target="_blank" rel="noreferrer">Link</a>' : '')
        +   '</div>'
        + '</div>'
        + '<button class="book-info-btn" data-book="' + i + '" data-action="info">?</button>'
        + '<div class="book-actions">' + btns + '</div>'
        + '</li>';
    }).join("");

    for (let r = 0; r < NUM_RANKS; r++) {
      document.getElementById("slot" + (r+1)).textContent = state.ranks[r] !== null ? BOOKS[state.ranks[r]].title : "\\u2014";
    }
    document.getElementById("slotVeto").textContent = state.veto !== null ? BOOKS[state.veto].title : "None";
    checkSubmit();
  }

  document.getElementById("displayName").addEventListener("input", checkSubmit);

  document.getElementById("bookList").addEventListener("click", function(e) {
    const btn = e.target.closest("button");
    if (!btn) return;
    const bookIdx = parseInt(btn.dataset.book);
    if (btn.dataset.action === "info") {
      // Toggle description
      const desc = document.getElementById("desc-" + bookIdx);
      if (desc) desc.classList.toggle("open");
      return;
    }
    if (btn.dataset.action === "veto") {
      state.veto = (state.veto === bookIdx) ? null : bookIdx;
      if (state.veto !== null) {
        const ri = state.ranks.indexOf(bookIdx);
        if (ri !== -1) state.ranks[ri] = null;
      }
    } else if (btn.dataset.rank) {
      const rank = parseInt(btn.dataset.rank) - 1;
      if (state.veto === bookIdx) state.veto = null;
      if (state.ranks[rank] === bookIdx) { state.ranks[rank] = null; }
      else {
        const prev = state.ranks.indexOf(bookIdx);
        if (prev !== -1) state.ranks[prev] = null;
        state.ranks[rank] = bookIdx;
      }
    }
    render();
  });

  document.getElementById("submitBtn").addEventListener("click", async function() {
    const name = getName();
    const errEl = document.getElementById("nameError");
    const msg = getMissingMessage();
    if (msg) {
      errEl.textContent = msg;
      errEl.style.display = "block";
      return;
    }
    errEl.style.display = "none";
    const toast = document.getElementById("toast");
    toast.style.display = "none";
    this.classList.add("not-ready");
    this.textContent = "Submitting...";
    try {
      const resp = await fetch("/vote/submit", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
          display_name: name,
          rank1: BOOKS[state.ranks[0]].title,
          rank2: BOOKS[state.ranks[1]].title,
          rank3: BOOKS[state.ranks[2]].title,
          rank4: BOOKS[state.ranks[3]].title,
          veto:  state.veto !== null ? BOOKS[state.veto].title : null,
        }),
      });
      const data = await resp.json();
      toast.style.display = "block";
      if (data.success) {
        state.hasSubmitted = true;
        toast.style.background = "rgba(124,58,46,.08)";
        toast.style.color = "var(--accent)";
        toast.textContent = data.updated
          ? "Vote updated for " + name + "."
          : "Vote submitted! Thanks, " + name + ".";
        this.textContent = "Submitted";
      } else {
        toast.style.background = "rgba(192,57,43,.08)";
        toast.style.color = "#c0392b";
        toast.textContent = data.detail || "Something went wrong. Please try again.";
        this.classList.remove("not-ready");
        this.textContent = "Submit Vote";
      }
    } catch(e) {
      toast.style.display = "block";
      toast.style.color = "#c0392b";
      toast.textContent = "Network error. Please try again.";
      this.classList.remove("not-ready");
      this.textContent = "Submit Vote";
    }
  });

  // --- Results tab ---
  function voteLabel(n) { return n + " vote" + (n === 1 ? "" : "s"); }

  // Shared by the live Results tab and frozen History snapshots.
  function buildRoundsHtml(rounds) {
    let html = "";
    rounds.forEach((round, ri) => {
      const sorted = Object.entries(round.counts).sort((a,b) => b[1] - a[1]);
      const total = round.active_ballots || 0;
      let rhtml = '<div class="round-block"><div class="round-title">Round ' + (ri+1) + '</div>';

      const elimList = Array.isArray(round.eliminated) ? round.eliminated : (round.eliminated ? [round.eliminated] : []);
      const counts2nd = round.counts_2nd || {};
      const counts3rd = round.counts_3rd || {};
      const counts4th = round.counts_4th || {};
      const ORDINAL_MAP = {2: "2nd", 3: "3rd", 4: "4th"};
      const tbUsed = round.tiebreak_used;
      sorted.forEach(([book, count]) => {
        let cls = "round-row";
        if (elimList.includes(book)) cls += " elim";
        if (book === round.winner) cls += " win";
        const sec = counts2nd[book];
        const third = counts3rd[book];
        const fourth = counts4th[book];
        const voteParts = [
          '<span class="round-vote-segment first">' + count + ' 1st</span>',
          '<span class="round-vote-segment second">' + (sec !== undefined ? sec : 0) + ' 2nd</span>',
          '<span class="round-vote-segment third">' + (third !== undefined ? third : 0) + ' 3rd</span>',
          '<span class="round-vote-segment fourth">' + (fourth !== undefined ? fourth : 0) + ' 4th</span>',
        ];
        rhtml += '<div class="' + cls + '">'
          + '<span class="round-name">' + _escHtml(book) + '</span>'
          + '<span class="round-votes">' + voteParts.join("") + '</span>'
          + '</div>';
      });

      if (round.tied_winners) {
        const tiedNames = Array.isArray(round.tied_winners) ? round.tied_winners : [round.tied_winners];
        rhtml += '<div class="round-reason">\\u003d\\u003d Unresolvable tie — ' + tiedNames.map(_escHtml).join(" and ")
          + ' are exactly tied. No winner can be determined by RCV alone.</div>';
      } else if (round.winner) {
        const winCount = round.counts[round.winner] || 0;
        let winNote = ".";
        if (tbUsed === "backup") winNote = " after a tie was broken by total backup votes (2nd+3rd+4th place).";
        else if (tbUsed) winNote = " after a tie was broken by " + ORDINAL_MAP[tbUsed] + "-place votes.";
        else if (winCount > total / 2) winNote = " — majority reached.";
        else if (sorted.length <= 2) winNote = " — wins the final head-to-head.";
        rhtml += '<div class="round-reason">\\u2714 ' + _escHtml(round.winner)
          + ' wins with ' + voteLabel(winCount) + winNote + '</div>';
      } else if (elimList.length > 0) {
        let tbNote = "";
        if (tbUsed === "backup") tbNote = " Tie broken by total backup votes (2nd+3rd+4th place).";
        else if (tbUsed) tbNote = " Tie broken by " + ORDINAL_MAP[tbUsed] + "-place votes.";
        if (elimList.length === 1) {
          const elimCount = round.counts[elimList[0]] || 0;
          rhtml += '<div class="round-reason">\\u2716 ' + _escHtml(elimList[0])
            + ' eliminated (fewest first-choice votes: ' + voteLabel(elimCount)
            + ').' + tbNote + ' Ballots transfer to next choice.</div>';
        } else {
          rhtml += '<div class="round-reason">\\u2716 ' + elimList.map(_escHtml).join(", ")
            + ' eliminated (tied for fewest votes).' + tbNote + ' Ballots transfer to next choices.</div>';
        }
      }

      rhtml += "</div>";
      html += rhtml;
    });
    return html;
  }

  function buildRankingHtml(ranking) {
    const ordered = (ranking || []).slice().reverse();
    const rankClass = ["r1","r2","r3"];
    return ordered.map((book, i) => {
      const rc = i < 3 ? rankClass[i] : "";
      const extra = i === 0 ? " winner" : "";
      return '<li class="result-item' + extra + '">'
        + '<div class="result-rank ' + rc + '">' + (i+1) + '</div>'
        + '<div class="result-book">' + _escHtml(book) + '</div>'
        + '</li>';
    }).join("");
  }

  async function loadResults() {
    const list = document.getElementById("resultsList");
    const subtitle = document.getElementById("resultsSubtitle");
    const topTwo = document.getElementById("topTwo");
    list.innerHTML = "";
    topTwo.innerHTML = "";
    subtitle.textContent = "Loading...";
    try {
      const resp = await fetch("/vote/results/data");
      const data = await resp.json();
      const ranking = data.ranking || [];
      const rounds = data.rounds || [];
      const vetoed = data.vetoed || [];
      const totalBallots = data.total_ballots || 0;

      if (!totalBallots) {
        list.innerHTML = "<li class=\\"results-empty\\">No votes yet.</li>";
        subtitle.textContent = "0 votes cast";
        return;
      }

      subtitle.textContent = "";

      // Work out who still hasn't voted
      const voters = data.voters || [];
      const votedFirstNames = voters.map(v => v.split(/\\s+/)[0].toLowerCase());
      const awaiting = EXPECTED_VOTERS.filter(n => !votedFirstNames.includes(n.toLowerCase()));
      const allIn = awaiting.length === 0;

      // Voting in progress banner
      if (!allIn) {
        const voted = EXPECTED_VOTERS.length - awaiting.length;
        topTwo.innerHTML = "<div class=\\"voting-progress-banner\\">"
          + "<div class=\\"voting-progress-dot\\"></div>"
          + "<div class=\\"voting-progress-text\\">Voting in progress &mdash; "
          + voted + " of " + EXPECTED_VOTERS.length + " votes cast. Results may change.</div>"
          + "</div>";
      } else {
        topTwo.innerHTML = "";
      }

      // Top 2 (or 3) hero cards
      const finalRound = rounds.length ? rounds[rounds.length - 1] : null;
      const ordered = ranking.slice().reverse();
      const isTiedFinale = finalRound && Array.isArray(finalRound.tied_winners);
      const tiedCount = isTiedFinale ? finalRound.tied_winners.length : 0;
      if (ordered.length >= 2 && finalRound) {
        const c = finalRound.counts || {};
        let suffix;
        if (isTiedFinale) {
          suffix = "— it's a tie!";
        } else {
          suffix = allIn ? "in final round" : "so far";
        }
        const makeCard = (cls, label, book) =>
          "<div class=\\"top-card " + cls + "\\">"
          + "<div class=\\"top-label\\">" + label + "</div>"
          + "<div class=\\"top-book\\">" + book + "</div>"
          + "<div class=\\"top-votes\\">" + voteLabel(c[book] || 0) + " " + suffix + "</div>"
          + "</div>";
        let cards;
        if (isTiedFinale && tiedCount >= 3 && ordered.length >= 3) {
          cards = makeCard("gold", "Tied", ordered[0])
                + makeCard("silver", "Tied", ordered[1])
                + makeCard("bronze", "Tied", ordered[2]);
        } else {
          const label1 = isTiedFinale ? "Tied" : (allIn ? "Winner" : "Currently Leading");
          const label2 = isTiedFinale ? "Tied" : (allIn ? "Runner-up" : "In Second Place");
          cards = makeCard("gold", label1, ordered[0]) + makeCard("silver", label2, ordered[1]);
        }
        topTwo.innerHTML += "<div class=\\"top-two\\">" + cards + "</div>";
      }

      // Awaiting section
      if (awaiting.length > 0) {
        topTwo.innerHTML += "<div class=\\"awaiting-block\\">"
          + "<div class=\\"awaiting-label\\">Awaiting votes from</div>"
          + "<div class=\\"awaiting-names\\">" + awaiting.join(", ") + "</div>"
          + "</div>";
      }

      let html = "";

      // Vetoed books — only shown once all votes are in
      if (allIn && vetoed.length) {
        html += "<div class=\\"results-section-title\\">Vetoed (removed before counting)</div>";
        vetoed.forEach(book => {
          html += "<li class=\\"result-item vetoed-item\\">"
            + "<div class=\\"result-rank\\">\\u2718</div>"
            + "<div class=\\"result-book\\">" + book + "</div>"
            + "</li>";
        });
      }

      // Rounds detail — only reveal once every vote is in
      if (allIn && rounds.length) {
        html += "<div class=\\\"results-section-title\\\">How it played out</div>";
        html += buildRoundsHtml(rounds);
      }

      // Full ranking — only shown once all votes are in
      if (allIn) {
        html += "<div class=\\"results-section-title\\">Final Ranking</div>";
        html += buildRankingHtml(ranking);
      }

      list.innerHTML = html;
      await initCarousel(!allIn);
    } catch(e) {
      subtitle.textContent = "Failed to load";
    }
  }

  // --- Waiting-room card carousel ---
  var _carouselCards = [];
  var _carouselIdx = 0;

  var SEED_CARDS = [];

  function _escHtml(s) {
    return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
  }

  function _hopRabbit() {
    var r = document.getElementById("carouselRabbit");
    if (!r) return;
    r.classList.remove("hopping");
    void r.offsetHeight;
    r.classList.add("hopping");
    setTimeout(function(){ r.classList.remove("hopping"); }, 1300);
  }

  function _renderCarouselCard(idx) {
    var card = document.getElementById("carouselCard");
    var dots = document.getElementById("carouselDots");
    if (!card || !_carouselCards.length) return;
    var c = _carouselCards[idx];
    var deleteBtn = c.id
      ? '<button class="card-delete-btn" data-id="' + c.id + '" title="Delete this card">\u00d7</button>'
      : "";
    card.innerHTML = deleteBtn
      + '<div class="card-text">\u201c' + _escHtml(c.text) + '\u201d</div>'
      + '<div class="card-author">\u2014 ' + _escHtml(c.author) + '</div>';
    card.style.animation = "none";
    void card.offsetHeight;
    card.style.animation = "";
    if (dots) dots.textContent = (idx + 1) + " / " + _carouselCards.length;
    var db = card.querySelector(".card-delete-btn");
    if (db) db.addEventListener("click", async function() {
      if (!confirm("Delete this card? This cannot be undone.")) return;
      var resp = await fetch("/vote/cards/" + c.id, {method: "DELETE"});
      if (!resp.ok) { alert("Failed to delete card."); return; }
      _carouselCards.splice(idx, 1);
      if (!_carouselCards.length) {
        var stage = document.getElementById("carouselStage");
        if (stage) stage.style.display = "none";
        return;
      }
      _carouselIdx = Math.min(idx, _carouselCards.length - 1);
      _renderCarouselCard(_carouselIdx);
    });
  }

  async function initCarousel(isWaiting) {
    var wrap = document.getElementById("cardCarousel");
    if (!wrap) return;
    var dbCards = [];
    try {
      var cr = await fetch("/vote/cards");
      var cd = await cr.json();
      dbCards = (cd.cards || []).slice().reverse();
    } catch(e) {}
    _carouselCards = SEED_CARDS.concat(dbCards.map(function(c){ return {text:c.text, author:c.author, id:c.id}; }));
    _carouselIdx = 0;
    var ctaText = isWaiting
      ? "While we await the final votes &mdash; browse some cards &#8594;"
      : "Browse some cards &#8594;";
    wrap.innerHTML =
      '<div class="card-carousel-wrap">'
      + '<div class="card-carousel-cta" id="carouselCTA">' + ctaText + '</div>'
      + '<div id="carouselStage" style="display:none;width:100%;">'
      +   '<div class="card-stage"><div id="carouselCard" class="carousel-card"></div></div>'
      +   '<div class="rabbit-gif" id="carouselRabbit"></div>'
      +   '<div class="carousel-nav" id="carouselNav">'
      +     '<button id="carouselPrev">&#8592;</button>'
      +     '<div class="carousel-dots" id="carouselDots"></div>'
      +     '<button id="carouselNext">&#8594;</button>'
      +   '</div>'
      + '</div>'
      + '<div class="add-card-wrap" id="addCardWrap" style="display:none;">'
      +   '<button class="add-card-btn" id="addCardBtn">+ Add a card</button>'
      +   '<div class="add-card-form" id="addCardForm">'
      +     '<p class="add-card-prompt">Add something funny, interesting, or share who you think is most likely to be kicked out of the club.</p>'
      +     '<textarea id="cardText" placeholder="Your thought..." maxlength="280"></textarea>'
      +     '<div class="char-count"><span id="cardCharCount">0</span> / 280</div>'
      +     '<div class="add-card-actions">'
      +       '<button class="add-card-cancel" id="addCardCancel">Cancel</button>'
      +       '<button class="add-card-submit" id="addCardSubmit">Add Card</button>'
      +     '</div>'
      +   '</div>'
      + '</div>'
      + '</div>';
    document.getElementById("carouselCTA").addEventListener("click", function(){
      this.style.display = "none";
      var stage = document.getElementById("carouselStage");
      var addWrap = document.getElementById("addCardWrap");
      if (stage) stage.style.display = "";
      if (addWrap) addWrap.style.display = "";
      _renderCarouselCard(_carouselIdx);
      document.getElementById("carouselPrev").addEventListener("click", function(){
        _carouselIdx = (_carouselIdx - 1 + _carouselCards.length) % _carouselCards.length;
        _renderCarouselCard(_carouselIdx);
        _hopRabbit();
      });
      document.getElementById("carouselNext").addEventListener("click", function(){
        _carouselIdx = (_carouselIdx + 1) % _carouselCards.length;
        _renderCarouselCard(_carouselIdx);
        _hopRabbit();
      });
      document.getElementById("addCardBtn").addEventListener("click", function(){
        document.getElementById("addCardForm").classList.add("open");
        this.style.display = "none";
      });
      document.getElementById("addCardCancel").addEventListener("click", function(){
        document.getElementById("addCardForm").classList.remove("open");
        document.getElementById("addCardBtn").style.display = "";
        document.getElementById("cardText").value = "";
        document.getElementById("cardCharCount").textContent = "0";
      });
      document.getElementById("cardText").addEventListener("input", function(){
        document.getElementById("cardCharCount").textContent = this.value.length;
      });
      document.getElementById("addCardSubmit").addEventListener("click", async function(){
        var text = (document.getElementById("cardText").value || "").trim();
        if (!text) return;
        var author = (document.getElementById("displayName").value || "").trim() || "Anonymous";
        this.textContent = "Adding...";
        this.disabled = true;
        try {
          var resp = await fetch("/vote/cards", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({author: author, text: text})
          });
          if (!resp.ok) throw new Error("fail");
          var result = await resp.json();
          _carouselCards.push({text: result.card.text, author: result.card.author});
          _carouselIdx = _carouselCards.length - 1;
          document.getElementById("addCardForm").classList.remove("open");
          document.getElementById("addCardBtn").style.display = "";
          document.getElementById("cardText").value = "";
          document.getElementById("cardCharCount").textContent = "0";
          _renderCarouselCard(_carouselIdx);
          _hopRabbit();
        } catch(e) {}
        this.textContent = "Add Card";
        this.disabled = false;
      });
    });
  }

  // --- Admin: votes viewer (uses the stored admin password) ---
  async function loadAdminBallots() {
    const table = document.getElementById("adminBallotTable");
    const body = document.getElementById("adminBallotBody");
    const empty = document.getElementById("adminBallotEmpty");
    empty.style.display = "none";
    table.style.display = "none";
    try {
      const resp = await fetch("/vote/ballots?password=" + encodeURIComponent(_adminPw), {method: "POST"});
      if (!resp.ok) { empty.style.display = "block"; empty.textContent = "Could not load votes."; return; }
      const data = await resp.json();
      const ballots = data.ballots || [];
      if (!ballots.length) { empty.style.display = "block"; empty.textContent = "No votes yet."; return; }
      body.innerHTML = ballots.map(b => {
        const safeVoter = _escHtml(b.voter);
        return "<tr>"
          + "<td>" + _escHtml(b.voter) + "</td>"
          + "<td>" + _escHtml(b.rank1||"") + "</td>"
          + "<td>" + _escHtml(b.rank2||"") + "</td>"
          + "<td>" + _escHtml(b.rank3||"") + "</td>"
          + "<td>" + _escHtml(b.rank4||"") + "</td>"
          + "<td class=\\"veto-cell\\">" + _escHtml(b.veto||"\\u2014") + "</td>"
          + "<td><button class=\\"ballot-delete-btn\\" data-voter=\\"" + safeVoter + "\\" title=\\"Delete vote\\">\\u2715</button></td>"
          + "</tr>";
      }).join("");
      table.style.display = "table";
    } catch(e) {
      empty.style.display = "block"; empty.textContent = "Network error.";
    }
  }

  document.getElementById("adminBallotBody").addEventListener("click", async function(e) {
    const btn = e.target.closest(".ballot-delete-btn");
    if (!btn) return;
    const voter = btn.dataset.voter;
    if (!confirm("Delete the vote submitted by \\u201c" + voter + "\\u201d?\\n\\nThis cannot be undone.")) return;
    try {
      const resp = await fetch("/vote/ballot/" + encodeURIComponent(voter) + "?password=" + encodeURIComponent(_adminPw), {method: "DELETE"});
      if (!resp.ok) { alert("Failed to delete vote."); return; }
      await loadAdminBallots();
    } catch(e) {
      alert("Network error.");
    }
  });

  document.getElementById("refreshBtn").addEventListener("click", loadResults);

  // --- Suggest tab (public, read-only list) ---
  async function loadSuggestions() {
    const list = document.getElementById("suggestionList");
    const empty = document.getElementById("suggestionEmpty");
    try {
      const resp = await fetch("/vote/suggestions");
      const data = await resp.json();
      const items = data.suggestions || [];
      empty.style.display = items.length ? "none" : "block";
      list.innerHTML = items.map(function(s) {
        return '<li class="book-item">'
          + '<div class="book-badge">&#10047;</div>'
          + '<div class="book-info">'
          +   '<div class="book-title">' + _escHtml(s.title) + '</div>'
          +   '<div class="book-author">' + _escHtml(s.author)
          +     (s.suggested_by ? ' &mdash; suggested by ' + _escHtml(s.suggested_by) : '') + '</div>'
          +   (s.desc ? '<div class="book-desc open">' + _escHtml(s.desc) + '</div>' : '')
          +   (s.url ? '<a class="book-link" href="' + _escHtml(s.url) + '" target="_blank" rel="noreferrer">Link</a>' : '')
          + '</div>'
          + '</li>';
      }).join("");
    } catch(e) {
      list.innerHTML = "";
      empty.style.display = "block";
    }
  }

  document.getElementById("sgSubmit").addEventListener("click", async function() {
    const toast = document.getElementById("sgToast");
    const title = document.getElementById("sgTitle").value.trim();
    const author = document.getElementById("sgAuthor").value.trim();
    toast.style.display = "none";
    if (!title || !author) {
      toast.style.display = "block";
      toast.style.color = "#c0392b";
      toast.textContent = "Title and author are required.";
      return;
    }
    this.disabled = true;
    this.textContent = "Suggesting...";
    try {
      const resp = await fetch("/vote/suggest", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
          title: title,
          author: author,
          url: document.getElementById("sgUrl").value.trim() || null,
          note: document.getElementById("sgNote").value.trim() || null,
          suggested_by: document.getElementById("sgName").value.trim() || null,
        }),
      });
      const data = await resp.json();
      toast.style.display = "block";
      if (resp.ok) {
        toast.style.color = "var(--accent)";
        toast.textContent = "Suggestion added! It joins the ballot once approved.";
        document.getElementById("sgTitle").value = "";
        document.getElementById("sgAuthor").value = "";
        document.getElementById("sgUrl").value = "";
        document.getElementById("sgNote").value = "";
        loadSuggestions();
      } else {
        toast.style.color = "#c0392b";
        toast.textContent = data.detail || "Could not save suggestion.";
      }
    } catch(e) {
      toast.style.display = "block";
      toast.style.color = "#c0392b";
      toast.textContent = "Network error. Please try again.";
    }
    this.disabled = false;
    this.textContent = "Suggest Book";
  });

  // --- History tab ---
  async function loadHistory() {
    const wrap = document.getElementById("historyList");
    const empty = document.getElementById("historyEmpty");
    wrap.innerHTML = "";
    try {
      const resp = await fetch("/vote/history");
      const data = await resp.json();
      const rounds = data.rounds || [];
      empty.style.display = rounds.length ? "none" : "block";
      wrap.innerHTML = rounds.map(function(r) {
        const date = r.created_at
          ? new Date(r.created_at + "Z").toLocaleDateString(undefined, {year: "numeric", month: "long", day: "numeric"})
          : "";
        return '<div class="round-block">'
          + '<div class="round-title">' + (r.label ? _escHtml(r.label) : "Round #" + r.id) + (date ? ' &mdash; ' + date : '') + '</div>'
          + '<div class="history-winner">Winner: <strong>' + _escHtml(r.winner || "\\u2014") + '</strong> &middot; ' + r.total_ballots + ' ballots</div>'
          + '<button class="results-refresh history-detail-btn" data-id="' + r.id + '">Show details</button>'
          + '<div class="history-detail" id="hist-detail-' + r.id + '" style="display:none"></div>'
          + '</div>';
      }).join("");
    } catch(e) {
      wrap.innerHTML = '<div class="results-empty">Failed to load history.</div>';
    }
  }

  function buildHistoryDetail(snap) {
    const res = snap.results || {};
    let html = "";
    const vetoed = res.vetoed || [];
    if (vetoed.length) {
      html += '<div class="results-section-title">Vetoed (removed before counting)</div><ul class="results-list">';
      vetoed.forEach(function(book) {
        html += '<li class="result-item vetoed-item"><div class="result-rank">\\u2718</div>'
          + '<div class="result-book">' + _escHtml(book) + '</div></li>';
      });
      html += '</ul>';
    }
    if ((res.rounds || []).length) {
      html += '<div class="results-section-title">How it played out</div>' + buildRoundsHtml(res.rounds);
    }
    html += '<div class="results-section-title">Final Ranking</div>'
      + '<ul class="results-list">' + buildRankingHtml(res.ranking || []) + '</ul>';
    const ballots = snap.ballots || [];
    if (ballots.length) {
      html += '<div class="results-section-title">Ballots</div>'
        + '<table class="ballot-table" style="display:table">'
        + '<thead><tr><th>Voter</th><th>1st</th><th>2nd</th><th>3rd</th><th>4th</th><th>Veto</th></tr></thead><tbody>'
        + ballots.map(function(b) {
            return '<tr><td>' + _escHtml(b.voter) + '</td>'
              + '<td>' + _escHtml(b.rank1 || "") + '</td>'
              + '<td>' + _escHtml(b.rank2 || "") + '</td>'
              + '<td>' + _escHtml(b.rank3 || "") + '</td>'
              + '<td>' + _escHtml(b.rank4 || "") + '</td>'
              + '<td class="veto-cell">' + _escHtml(b.veto || "\\u2014") + '</td></tr>';
          }).join("")
        + '</tbody></table>';
    }
    const cards = snap.cards || [];
    if (cards.length) {
      html += '<div class="results-section-title">Cards from the waiting room</div>';
      cards.forEach(function(c) {
        html += '<div class="carousel-card" style="margin-bottom:10px">'
          + '<div class="card-text">\\u201c' + _escHtml(c.text) + '\\u201d</div>'
          + '<div class="card-author">\\u2014 ' + _escHtml(c.author) + '</div>'
          + '</div>';
      });
    }
    return html;
  }

  document.getElementById("historyList").addEventListener("click", async function(e) {
    const btn = e.target.closest(".history-detail-btn");
    if (!btn) return;
    const box = document.getElementById("hist-detail-" + btn.dataset.id);
    if (!box) return;
    if (box.style.display !== "none") {
      box.style.display = "none";
      btn.textContent = "Show details";
      return;
    }
    if (!box.dataset.loaded) {
      btn.textContent = "Loading...";
      try {
        const resp = await fetch("/vote/history/" + btn.dataset.id);
        if (!resp.ok) throw new Error("fail");
        box.innerHTML = buildHistoryDetail(await resp.json());
        box.dataset.loaded = "1";
      } catch(err) {
        box.innerHTML = '<div class="results-empty">Failed to load details.</div>';
      }
    }
    box.style.display = "";
    btn.textContent = "Hide details";
  });

  // --- Admin tab ---
  async function _verifyAdmin(pw) {
    try {
      const resp = await fetch("/vote/admin/check?password=" + encodeURIComponent(pw), {method: "POST"});
      return resp.ok;
    } catch(e) { return false; }
  }

  function showAdminDashboard(on) {
    document.getElementById("adminGate").style.display = on ? "none" : "";
    document.getElementById("adminDashboard").style.display = on ? "" : "none";
  }

  function refreshAdmin() {
    renderAdminStatus();
    renderAdminBooks();
    renderAdminSuggestions();
    loadAdminBallots();
    renderAdminHistory();
  }

  // Called when the Admin tab is opened.
  function openAdminTab() {
    showAdminDashboard(adminUnlocked);
    if (adminUnlocked) refreshAdmin();
    else document.getElementById("adminPw").focus();
  }

  async function unlockAdmin(pw) {
    if (!(await _verifyAdmin(pw))) return false;
    _adminPw = pw;
    adminUnlocked = true;
    try { localStorage.setItem("bc_admin_pw", pw); } catch(e) {}
    showAdminDashboard(true);
    refreshAdmin();
    return true;
  }

  function lockAdmin() {
    adminUnlocked = false;
    _adminPw = "";
    try { localStorage.removeItem("bc_admin_pw"); } catch(e) {}
    closeBookForm();
    showAdminDashboard(false);
  }

  document.getElementById("adminUnlockBtn").addEventListener("click", async function() {
    const err = document.getElementById("adminGateError");
    err.style.display = "none";
    const pw = document.getElementById("adminPw").value;
    if (!pw) return;
    this.disabled = true; this.textContent = "Unlocking...";
    const ok = await unlockAdmin(pw);
    if (!ok) { err.style.display = "block"; err.textContent = "Wrong password."; }
    document.getElementById("adminPw").value = "";
    this.disabled = false; this.textContent = "Unlock";
  });
  document.getElementById("adminPw").addEventListener("keydown", function(e) {
    if (e.key === "Enter") document.getElementById("adminUnlockBtn").click();
  });
  document.getElementById("adminLockBtn").addEventListener("click", lockAdmin);

  async function initAdmin() {
    if (_adminPw && await _verifyAdmin(_adminPw)) {
      adminUnlocked = true;
      if (document.getElementById("tab-admin").classList.contains("active")) openAdminTab();
    } else {
      adminUnlocked = false;
      _adminPw = "";
    }
  }

  // --- Admin: status toggles ---
  function renderAdminStatus() {
    const vOpen = votingOpen(), sOpen = suggestionsOpen();
    const vl = document.getElementById("votingStateLabel");
    vl.textContent = vOpen ? "Open \\u2014 people can vote" : "Closed";
    vl.className = "admin-toggle-sub " + (vOpen ? "open" : "closed");
    document.getElementById("votingToggle").textContent = vOpen ? "Close voting" : "Open voting";
    const sl = document.getElementById("suggestStateLabel");
    sl.textContent = sOpen ? "Open \\u2014 people can suggest" : "Closed";
    sl.className = "admin-toggle-sub " + (sOpen ? "open" : "closed");
    document.getElementById("suggestToggle").textContent = sOpen ? "Close suggestions" : "Open suggestions";
  }

  async function setSetting(key, value) {
    try {
      const resp = await fetch("/vote/settings?password=" + encodeURIComponent(_adminPw), {
        method: "POST", headers: {"Content-Type": "application/json"},
        body: JSON.stringify({key: key, value: value})
      });
      if (!resp.ok) { alert("Could not change setting."); return; }
      SETTINGS[key] = value;
      renderAdminStatus();
      applyGating();
    } catch(e) { alert("Network error."); }
  }

  document.getElementById("votingToggle").addEventListener("click", function() {
    setSetting("voting_open", votingOpen() ? "0" : "1");
  });
  document.getElementById("suggestToggle").addEventListener("click", function() {
    setSetting("suggestions_open", suggestionsOpen() ? "0" : "1");
  });

  // --- Admin: books (active ballot) ---
  function bookById(id) {
    id = parseInt(id);
    for (var i = 0; i < BOOKS.length; i++) { if (BOOKS[i].id === id) return BOOKS[i]; }
    return null;
  }

  function renderAdminBooks() {
    const list = document.getElementById("adminBookList");
    if (!BOOKS.length) {
      list.innerHTML = '<li class="results-empty" style="display:block;padding:16px">No books on the ballot yet.</li>';
      return;
    }
    list.innerHTML = BOOKS.map(function(b, i) {
      return '<li class="book-item">'
        + '<div class="book-badge">' + (i + 1) + '</div>'
        + '<div class="book-info">'
        +   '<div class="book-title">' + _escHtml(b.title) + '</div>'
        +   '<div class="book-author">' + _escHtml(b.author) + (b.pages ? ' &middot; ' + b.pages + ' pages' : '') + '</div>'
        + '</div>'
        + '<div class="book-actions">'
        +   '<button class="admin-book-btn" data-id="' + b.id + '" data-act="edit">Edit</button>'
        +   '<button class="admin-book-btn admin-del" data-id="' + b.id + '" data-act="del">Remove</button>'
        + '</div>'
        + '</li>';
    }).join("");
  }

  document.getElementById("adminBookList").addEventListener("click", function(e) {
    const btn = e.target.closest("button"); if (!btn) return;
    const book = bookById(btn.dataset.id); if (!book) return;
    if (btn.dataset.act === "edit") openBookForm(book);
    else if (btn.dataset.act === "del") deleteBookAdmin(book);
  });

  let _editingBookId = null;

  function openBookForm(book) {
    _editingBookId = book ? book.id : null;
    document.getElementById("bfTitle").value = book ? book.title : "";
    document.getElementById("bfAuthor").value = book ? book.author : "";
    document.getElementById("bfPages").value = book && book.pages ? book.pages : "";
    document.getElementById("bfUrl").value = book ? (book.url || "") : "";
    document.getElementById("bfDesc").value = book ? (book.desc || "") : "";
    document.getElementById("bfError").style.display = "none";
    document.getElementById("bookForm").style.display = "";
    document.getElementById("addBookBtn").style.display = "none";
    document.getElementById("bfTitle").focus();
  }

  function closeBookForm() {
    _editingBookId = null;
    const form = document.getElementById("bookForm");
    if (form) form.style.display = "none";
    const btn = document.getElementById("addBookBtn");
    if (btn) btn.style.display = "";
  }

  document.getElementById("addBookBtn").addEventListener("click", function() { openBookForm(null); });
  document.getElementById("bfCancel").addEventListener("click", closeBookForm);

  document.getElementById("bfSave").addEventListener("click", async function() {
    const errEl = document.getElementById("bfError");
    errEl.style.display = "none";
    const title = document.getElementById("bfTitle").value.trim();
    const author = document.getElementById("bfAuthor").value.trim();
    if (!title || !author) {
      errEl.style.display = "block";
      errEl.textContent = "Title and author are required.";
      return;
    }
    const pages = parseInt(document.getElementById("bfPages").value, 10);
    const payload = {
      title: title,
      author: author,
      pages: isNaN(pages) ? null : pages,
      desc: document.getElementById("bfDesc").value.trim() || null,
      url: document.getElementById("bfUrl").value.trim() || null,
    };
    const isEdit = _editingBookId !== null;
    const url = isEdit
      ? "/vote/books/" + _editingBookId + "?password=" + encodeURIComponent(_adminPw)
      : "/vote/books?password=" + encodeURIComponent(_adminPw);
    try {
      const resp = await fetch(url, {
        method: isEdit ? "PUT" : "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(payload),
      });
      if (!resp.ok) {
        const data = await resp.json();
        errEl.style.display = "block";
        errEl.textContent = data.detail || "Could not save book.";
        return;
      }
      closeBookForm();
      await loadBooks();
    } catch(e) {
      errEl.style.display = "block";
      errEl.textContent = "Network error.";
    }
  });

  async function deleteBookAdmin(book) {
    if (!confirm('Remove \\u201c' + book.title + '\\u201d from the ballot?')) return;
    try {
      const resp = await fetch("/vote/books/" + book.id + "?password=" + encodeURIComponent(_adminPw), {method: "DELETE"});
      if (!resp.ok) {
        const data = await resp.json();
        alert(data.detail || "Could not remove book.");
        return;
      }
      await loadBooks();
    } catch(e) {
      alert("Network error.");
    }
  }

  // --- Admin: pending suggestions ---
  async function renderAdminSuggestions() {
    const list = document.getElementById("adminSuggestionList");
    const empty = document.getElementById("adminSuggestionEmpty");
    try {
      const items = (await (await fetch("/vote/suggestions")).json()).suggestions || [];
      empty.style.display = items.length ? "none" : "block";
      list.innerHTML = items.map(function(s) {
        return '<li class="book-item">'
          + '<div class="book-badge">&#10047;</div>'
          + '<div class="book-info">'
          +   '<div class="book-title">' + _escHtml(s.title) + '</div>'
          +   '<div class="book-author">' + _escHtml(s.author) + (s.suggested_by ? ' &mdash; ' + _escHtml(s.suggested_by) : '') + '</div>'
          +   (s.desc ? '<div class="book-desc open">' + _escHtml(s.desc) + '</div>' : '')
          + '</div>'
          + '<div class="book-actions">'
          +   '<button class="admin-book-btn admin-approve" data-id="' + s.id + '" data-act="approve">Approve</button>'
          +   '<button class="admin-book-btn admin-del" data-id="' + s.id + '" data-act="reject">Reject</button>'
          + '</div>'
          + '</li>';
      }).join("");
    } catch(e) { list.innerHTML = ""; empty.style.display = "block"; }
  }

  document.getElementById("adminSuggestionList").addEventListener("click", async function(e) {
    const btn = e.target.closest("button"); if (!btn) return;
    const id = btn.dataset.id;
    if (btn.dataset.act === "approve") {
      const resp = await fetch("/vote/books/" + id + "/approve?password=" + encodeURIComponent(_adminPw), {method: "POST"});
      if (!resp.ok) { alert("Approve failed."); return; }
      await loadBooks();
      renderAdminSuggestions();
    } else if (btn.dataset.act === "reject") {
      if (!confirm("Reject this suggestion? It will be deleted.")) return;
      const resp = await fetch("/vote/books/" + id + "?password=" + encodeURIComponent(_adminPw), {method: "DELETE"});
      if (!resp.ok) { alert("Reject failed."); return; }
      renderAdminSuggestions();
    }
  });

  // --- Admin: history management ---
  async function renderAdminHistory() {
    const wrap = document.getElementById("adminHistoryList");
    const empty = document.getElementById("adminHistoryEmpty");
    wrap.innerHTML = "";
    try {
      const rounds = (await (await fetch("/vote/history")).json()).rounds || [];
      empty.style.display = rounds.length ? "none" : "block";
      wrap.innerHTML = rounds.map(function(r) {
        const date = r.created_at
          ? new Date(r.created_at + "Z").toLocaleDateString(undefined, {year: "numeric", month: "short", day: "numeric"})
          : "";
        return '<div class="admin-hist-row">'
          + '<div class="admin-hist-name">' + (r.label ? _escHtml(r.label) : "Round #" + r.id)
          +   ' <span>' + (r.winner ? _escHtml(r.winner) : "no winner") + (date ? ' &middot; ' + date : '') + '</span></div>'
          + '<button class="admin-book-btn" data-id="' + r.id + '" data-act="rename">Rename</button>'
          + '<button class="admin-book-btn admin-del" data-id="' + r.id + '" data-act="delete">Delete</button>'
          + '</div>';
      }).join("");
    } catch(e) { wrap.innerHTML = '<div class="results-empty">Failed to load history.</div>'; }
  }

  document.getElementById("adminHistoryList").addEventListener("click", async function(e) {
    const btn = e.target.closest("button"); if (!btn) return;
    const id = btn.dataset.id;
    if (btn.dataset.act === "rename") {
      const label = prompt("New name for this round (blank to clear):");
      if (label === null) return;
      const resp = await fetch("/vote/history/" + id + "?password=" + encodeURIComponent(_adminPw), {
        method: "PUT", headers: {"Content-Type": "application/json"}, body: JSON.stringify({label: label})
      });
      if (!resp.ok) { alert("Rename failed."); return; }
      renderAdminHistory();
    } else if (btn.dataset.act === "delete") {
      if (!confirm("Delete this archived round permanently?")) return;
      const resp = await fetch("/vote/history/" + id + "?password=" + encodeURIComponent(_adminPw), {method: "DELETE"});
      if (!resp.ok) { alert("Delete failed."); return; }
      renderAdminHistory();
    }
  });

  // --- Admin: end the round ---
  async function doReset(archive) {
    const q1 = archive
      ? "Archive this round to History, then clear the ballot?"
      : "Clear the ballot WITHOUT saving to History? This cannot be undone.";
    if (!confirm(q1)) return;
    if (!confirm("Are you sure? The next round starts with an empty book list.")) return;
    const err = document.getElementById("resetError");
    err.style.display = "none";
    try {
      const resp = await fetch("/vote/reset?password=" + encodeURIComponent(_adminPw) + "&archive=" + (archive ? "true" : "false"), {method: "POST"});
      if (!resp.ok) throw new Error("fail");
      const data = await resp.json();
      alert(data.archived_round
        ? "Round archived. Winner: " + (data.winner || "\\u2014")
        : "Round cleared.");
      window.location.reload();
    } catch(e) {
      err.style.display = "block";
      err.textContent = "Reset failed.";
    }
  }
  document.getElementById("resetArchiveBtn").addEventListener("click", function() { doReset(true); });
  document.getElementById("resetPlainBtn").addEventListener("click", function() { doReset(false); });

  document.getElementById("curationSuggestBtn").addEventListener("click", function() {
    document.querySelector('.tab-btn[data-tab="suggest"]').click();
  });

  loadSettings();
  loadBooks();
  initAdmin();
})();
</script>
</div><!-- /vote-content-area -->
"""
