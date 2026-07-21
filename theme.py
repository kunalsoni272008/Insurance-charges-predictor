"""
Global CSS injected once per app run. Ports the color tokens, fonts,
glass 'surface' cards, and CSS keyframe animations from src/index.css.
"""

GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
  --bg: #0b1120;
  --surface: rgba(255, 255, 255, 0.055);
  --surface-hover: rgba(255, 255, 255, 0.095);
  --line: rgba(255, 255, 255, 0.09);
  --line-soft: rgba(255, 255, 255, 0.06);
  --muted: #8490a7;
  --muted-light: #aab3c5;
  --white: #f7f8fb;
  --blue: #87a9f0;
  --mint: #8ed8c1;
  --peach: #ef9f7a;
  --yellow: #f0c36e;
  --lilac: #af9eea;
  --radius: 17px;
}

/* ---- App shell ---- */
html, body, [data-testid="stAppViewContainer"], .stApp {
  background: var(--bg) !important;
  color: var(--white);
  font-family: 'Manrope', ui-sans-serif, system-ui, sans-serif;
}
[data-testid="stHeader"] { background: transparent; }
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #0d1729 0%, #0b1425 100%) !important;
  border-right: 1px solid var(--line-soft);
}
[data-testid="stSidebar"] > div { padding-top: 14px; }
.block-container { padding: 2rem 3rem 4rem; max-width: 1350px; }

/* ---- Typography helpers ---- */
.mono { font-family: 'DM Mono', monospace; }
.eyebrow, .section-label {
  margin: 0 0 10px; color: var(--blue); font-family: 'DM Mono', monospace;
  font-size: 10px; font-weight: 500; letter-spacing: .13em; text-transform: uppercase;
}
.page-title {
  max-width: 760px; margin: 0; color: var(--white);
  font-size: clamp(28px, 3.6vw, 44px); font-weight: 700; letter-spacing: -.045em; line-height: 1.08;
}
.page-description { max-width: 620px; margin: 12px 0 0; color: var(--muted); font-size: 13.5px; line-height: 1.75; }
em.hl { color: var(--mint); font-style: normal; }

/* ---- Surfaces / cards ---- */
.surface {
  background: linear-gradient(140deg, rgba(255,255,255,.072), rgba(255,255,255,.032));
  border: 1px solid var(--line); border-radius: var(--radius);
  box-shadow: 0 22px 60px rgba(0,0,0,.08);
  padding: 22px 24px;
}
.metric-card {
  min-height: 108px; padding: 16px 17px;
  background: linear-gradient(140deg, rgba(255,255,255,.065), rgba(255,255,255,.028));
  border: 1px solid var(--line); border-radius: 14px;
  transition: transform .23s ease, border-color .23s ease, background .23s ease;
}
.metric-card:hover { transform: translateY(-3px); border-color: rgba(255,255,255,.15); }
.metric-card-top { display: flex; align-items: center; justify-content: space-between; }
.metric-label { color: var(--muted); font-size: 10px; }
.metric-icon {
  display: grid; width: 24px; height: 24px; place-items: center; border-radius: 7px;
  color: var(--blue); background: rgba(135,169,240,.1);
}
.metric-value { margin-top: 12px; color: var(--white); font-size: 21px; font-weight: 700; letter-spacing: -.03em; }
.metric-meta { display: flex; align-items: center; gap: 7px; margin-top: 9px; color: #6f7d94; font-family: 'DM Mono', monospace; font-size: 9px; }
.trend-up { color: var(--mint); } .trend-down { color: var(--peach); }

.accent-blue .metric-icon { color: var(--blue); background: rgba(135,169,240,.1); }
.accent-mint .metric-icon { color: var(--mint); background: rgba(142,216,193,.1); }
.accent-peach .metric-icon { color: var(--peach); background: rgba(239,159,122,.1); }
.accent-lilac .metric-icon { color: var(--lilac); background: rgba(175,158,234,.1); }

/* ---- Tags ---- */
.tag {
  display: inline-flex; align-items: center; gap: 7px; padding: 6px 10px; border-radius: 7px;
  font-family: 'DM Mono', monospace; font-size: 10px; line-height: 1; white-space: nowrap;
}
.tag-blue { color: var(--blue); background: rgba(135,169,240,.1); border: 1px solid rgba(135,169,240,.16); }
.tag-mint { color: var(--mint); background: rgba(142,216,193,.1); border: 1px solid rgba(142,216,193,.16); }
.tag-yellow { color: var(--yellow); background: rgba(240,195,110,.1); border: 1px solid rgba(240,195,110,.15); }
.tag-peach { color: var(--peach); background: rgba(239,159,122,.1); border: 1px solid rgba(239,159,122,.15); }
.tag-neutral { color: var(--muted-light); background: rgba(255,255,255,.06); border: 1px solid var(--line); }
.tag-live-dot { width: 5px; height: 5px; border-radius: 50%; background: currentColor; box-shadow: 0 0 0 3px rgba(142,216,193,.08); display: inline-block; }

/* ---- Sidebar nav ---- */
.brand-lockup { display: flex; align-items: center; gap: 10px; padding: 4px 6px 22px; }
.brand-mark {
  position: relative; display: grid; width: 24px; height: 24px;
  grid-template-columns: repeat(2, 1fr); grid-template-rows: repeat(2, 1fr); gap: 3px;
  transform: rotate(-10deg);
}
.brand-mark span { display: block; border-radius: 4px; background: var(--white); }
.brand-mark span:nth-child(1) { grid-row: span 2; background: var(--mint); }
.brand-mark span:nth-child(2) { background: var(--blue); }
.brand-mark span:nth-child(3) { background: var(--peach); }
.brand-wordmark { font-size: 19px; font-weight: 800; letter-spacing: -.04em; color: var(--white); }

.workspace-switcher {
  display: flex; align-items: center; gap: 10px; margin: 0 3px 20px; padding: 9px 10px;
  background: rgba(255,255,255,.045); border: 1px solid var(--line-soft); border-radius: 12px;
}
.workspace-avatar {
  display: grid; place-items: center; width: 28px; height: 28px; border-radius: 8px;
  background: linear-gradient(145deg, #6285dd, #3d529b); color: white; font-size: 10px; font-weight: 800; flex: 0 0 auto;
}
.workspace-copy strong { display: block; font-size: 11px; color: var(--white); }
.workspace-copy span { font-size: 10px; color: var(--muted); }

.nav-caption {
  margin: 14px 11px 6px; color: #657189; font-family: 'DM Mono', monospace;
  font-size: 9px; font-weight: 500; letter-spacing: .12em; text-transform: uppercase;
}

/* Nav buttons: restyle Streamlit's own st.button to look like the original nav items */
section[data-testid="stSidebar"] .stButton button {
  width: 100%; text-align: left; justify-content: flex-start;
  color: #8994a9; background: transparent; border: 1px solid transparent; border-radius: 10px;
  font-size: 12.5px; font-weight: 500; padding: 9px 12px; transition: all .2s ease;
}
section[data-testid="stSidebar"] .stButton button:hover {
  color: var(--white); background: rgba(255,255,255,.06); border-color: transparent;
}
section[data-testid="stSidebar"] .stButton button:focus:not(:active) { color: var(--white); }
.nav-item-active button {
  color: var(--white) !important;
  background: linear-gradient(90deg, rgba(75, 113, 198, .23), rgba(75, 113, 198, .07)) !important;
  border-color: rgba(116, 151, 229, .13) !important;
}

.sidebar-bottom-block { margin-top: 18px; padding-top: 14px; border-top: 1px solid var(--line-soft); }
.support-link { display: flex; align-items: center; gap: 10px; padding: 8px 10px; color: #8792a8; font-size: 11px; }
.theme-row {
  display: flex; align-items: center; gap: 9px; padding: 12px 10px; margin: 8px 0;
  border-top: 1px solid var(--line-soft); border-bottom: 1px solid var(--line-soft);
  color: var(--muted); font-size: 10.5px;
}
.theme-icon {
  display: grid; place-items: center; width: 22px; height: 22px; border-radius: 7px;
  color: var(--yellow); background: rgba(240,195,110,.1);
}
.profile-row { display: flex; align-items: center; gap: 9px; padding: 10px 8px; }
.profile-avatar {
  width: 27px; height: 27px; border-radius: 50%; flex: 0 0 auto;
  background: linear-gradient(145deg, #c98371, #885e71);
  display: grid; place-items: center; color: white; font-size: 10px; font-weight: 800;
}
.profile-copy strong { display: block; font-size: 11px; color: var(--white); }
.profile-copy span { font-size: 10px; color: var(--muted); }

/* ---- Top bar ---- */
.topbar {
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 4px 22px; border-bottom: 1px solid var(--line-soft); margin-bottom: 26px;
}
.breadcrumbs { display: flex; align-items: center; gap: 10px; color: #78849a; font-size: 12px; }
.breadcrumbs strong { color: var(--muted-light); font-weight: 600; }
.system-status { display: flex; align-items: center; gap: 8px; color: #93a1b7; font-size: 10.5px; }
.live-pulse, .status-dot {
  display: inline-block; width: 6px; height: 6px; border-radius: 50%;
  background: var(--mint); box-shadow: 0 0 0 4px rgba(142,216,193,.1);
}
.live-pulse { animation: pulse 2.1s infinite; }
.status-dot-green { background: var(--mint); box-shadow: 0 0 0 4px rgba(142,216,193,.1); }

/* ---- Buttons (content area, not sidebar) ---- */
.block-container .stButton button {
  border-radius: 10px; font-weight: 700; font-size: 12px; min-height: 42px;
  background: linear-gradient(110deg, #94dbc3, #82cfe3); color: #0a1422; border: 1px solid rgba(255,255,255,.16);
  box-shadow: 0 10px 26px rgba(118, 207, 196, .14); transition: transform .2s ease;
}
.block-container .stButton button:hover { transform: translateY(-2px); }

/* ---- Hero (Home page) ---- */
.home-hero {
  position: relative; overflow: hidden; margin: -6px 0 22px; padding: 40px 44px;
  background: radial-gradient(circle at 90% 24%, rgba(110, 139, 220, .22), transparent 25rem),
              linear-gradient(112deg, #18253e 0%, #111c32 54%, #142642 100%);
  border: 1px solid rgba(137,166,231,.14); border-radius: 22px;
}
.hero-brand-line { display: flex; align-items: center; gap: 9px; margin-bottom: 20px; color: #b8c3d8; font-size: 10.5px; }
.hero-copy h1 { max-width: 620px; margin: 0; color: var(--white); font-size: clamp(32px, 4.2vw, 52px); font-weight: 700; letter-spacing: -.045em; line-height: 1.05; }
.hero-description { max-width: 480px; margin: 18px 0 22px; color: #a2aec1; font-size: 13.5px; line-height: 1.75; }
.hero-trust { display: flex; align-items: center; gap: 8px; margin-top: 20px; color: #73839d; font-size: 10px; }
.play-link { display: inline-flex; align-items: center; gap: 8px; color: #bdc7d8; font-size: 11.5px; margin-left: 16px; }

/* ---- Feature list / workflow ---- */
.feature-list { display: flex; flex-direction: column; gap: 12px; margin: 18px 0; }
.feature-list > div { display: flex; align-items: center; gap: 9px; color: #c3ccdc; font-size: 12.5px; }
.feature-check {
  display: grid; place-items: center; width: 19px; height: 19px; border-radius: 50%;
  background: rgba(142,216,193,.14); color: var(--mint); flex: 0 0 auto;
}
.workflow-step { display: flex; flex-direction: column; gap: 10px; }
.workflow-icon {
  display: grid; width: 34px; height: 34px; place-items: center; border-radius: 11px;
  font-family: 'DM Mono', monospace; font-size: 10px; font-weight: 600;
}
.workflow-icon-blue { color: var(--blue); background: rgba(135,169,240,.14); }
.workflow-icon-peach { color: var(--peach); background: rgba(239,159,122,.14); }
.workflow-icon-mint { color: var(--mint); background: rgba(142,216,193,.14); }
.workflow-step strong { display: block; color: var(--white); font-size: 12px; }
.workflow-step span { display: block; margin-top: 4px; color: var(--muted); font-size: 11px; }
.workflow-foot { display: flex; align-items: center; gap: 7px; margin-top: 22px; color: #75849c; font-family: 'DM Mono', monospace; font-size: 10px; }
.tech-strip { display: flex; align-items: center; justify-content: space-between; margin-top: 22px; padding: 16px 2px; border-top: 1px solid var(--line-soft); }
.tech-kicker { color: #64738b; font-family: 'DM Mono', monospace; font-size: 9px; text-transform: uppercase; letter-spacing: .1em; }
.tech-items { display: flex; gap: 20px; color: #6d7b92; font-family: 'DM Mono', monospace; font-size: 10.5px; }

/* ---- Chart header ---- */
.chart-header-title { color: #edf1f8; font-size: 14px; font-weight: 700; letter-spacing: -.01em; margin: 0; }
.chart-header-sub { color: #77849a; font-size: 10.5px; margin: 5px 0 0; }

/* ---- Prediction result panel ---- */
.result-empty {
  min-height: 420px; display: flex; flex-direction: column; align-items: flex-start; justify-content: center;
  padding: 10px 10px 10px 4px;
}
.result-orbit {
  display: grid; place-items: center; width: 56px; height: 56px; margin-bottom: 20px; color: var(--mint);
  background: radial-gradient(circle, rgba(142,216,193,.22), rgba(142,216,193,.03));
  border: 1px solid rgba(142,216,193,.3); border-radius: 50%;
  box-shadow: 0 0 0 12px rgba(142,216,193,.035), 0 0 0 24px rgba(142,216,193,.02);
  animation: orbFloat 4s ease-in-out infinite; font-size: 22px;
}
.result-empty h2 { max-width: 280px; margin: 0; color: var(--white); font-size: 25px; letter-spacing: -.03em; line-height: 1.15; }
.result-empty p { max-width: 300px; margin: 14px 0 20px; color: #97a6bf; font-size: 12px; line-height: 1.7; }
.result-note { margin-top: 20px; color: #6e7e9a; font-family: 'DM Mono', monospace; font-size: 9px; }

.result-amount { margin: 16px 0 20px; color: var(--white); font-size: clamp(34px, 3.6vw, 46px); font-weight: 700; letter-spacing: -.03em; }
.result-range { padding: 14px 0 18px; border-top: 1px solid rgba(255,255,255,.1); border-bottom: 1px solid rgba(255,255,255,.1); }
.result-range-labels { display: flex; justify-content: space-between; color: #8293ad; font-size: 10.5px; }
.result-range-labels strong { color: #c3ccdc; font-family: 'DM Mono', monospace; font-weight: 500; }
.range-track { height: 5px; margin: 12px 0 6px; overflow: hidden; background: rgba(255,255,255,.1); border-radius: 5px; }
.range-fill { display: block; height: 100%; background: linear-gradient(90deg, var(--blue), var(--mint)); border-radius: 5px; }
.range-scale { display: flex; justify-content: space-between; color: #6e7f99; font-family: 'DM Mono', monospace; font-size: 9px; }

.signal-list { display: flex; flex-direction: column; gap: 10px; margin-top: 14px; }
.signal-row { display: grid; grid-template-columns: 10px 1fr auto; align-items: center; gap: 8px; color: #9daac0; font-size: 11px; }
.signal-dot { width: 6px; height: 6px; border-radius: 50%; }
.signal-peach { background: var(--peach); } .signal-yellow { background: var(--yellow); } .signal-blue { background: var(--blue); }
.signal-strong { color: #b8c2d1; font-family: 'DM Mono', monospace; font-size: 9px; }

.recommendation {
  display: flex; gap: 10px; margin: 18px 0; padding: 12px;
  background: rgba(142,216,193,.055); border: 1px solid rgba(142,216,193,.12); border-radius: 10px;
}
.recommendation-icon { display: grid; place-items: center; width: 27px; height: 27px; flex: 0 0 auto; color: var(--mint); background: rgba(142,216,193,.12); border-radius: 7px; }
.recommendation strong { display: block; color: #cad6df; font-size: 10.5px; }
.recommendation p { margin: 4px 0 0; color: #8193a5; font-size: 10.5px; line-height: 1.55; }
.disclaimer { display: flex; align-items: center; justify-content: center; gap: 7px; margin-top: 16px; color: #67758a; font-size: 10.5px; }

/* ---- Analytics / performance small bits ---- */
.legend-row { display: flex; gap: 16px; margin-top: 14px; color: #7d8ba0; font-family: 'DM Mono', monospace; font-size: 9.5px; }
.legend-dot { display: inline-block; width: 6px; height: 6px; margin-right: 5px; border-radius: 50%; }
.legend-blue { background: var(--blue); } .legend-mint { background: var(--mint); }
.legend-yellow { background: var(--yellow); } .legend-peach { background: var(--peach); } .legend-lilac { background: var(--lilac); }
.analytics-note, .model-footnote {
  display: flex; align-items: center; justify-content: center; gap: 7px; margin-top: 18px;
  color: #68778e; font-family: 'DM Mono', monospace; font-size: 10px; text-align: center;
}

.performance-callout {
  display: flex; align-items: center; gap: 11px; margin-bottom: 14px; padding: 12px 14px;
  background: rgba(135,169,240,.07); border: 1px solid rgba(135,169,240,.13); border-radius: 11px;
}
.callout-icon { display: grid; place-items: center; width: 29px; height: 29px; color: var(--blue); background: rgba(135,169,240,.12); border-radius: 8px; }
.performance-callout strong { color: #c7d2e3; font-size: 11px; display: block; }
.performance-callout span { color: #7f8da5; font-size: 10.5px; }

.chart-insight { display: flex; align-items: center; gap: 8px; margin-top: 14px; padding: 10px; color: #8291a7; background: rgba(135,169,240,.045); border-radius: 7px; font-size: 10px; }
.chart-insight-warm { background: rgba(239,159,122,.045); }

.coefficient-row { display: grid; grid-template-columns: 100px 1fr 44px; align-items: center; gap: 10px; margin-bottom: 14px; }
.coefficient-name { display: flex; align-items: center; gap: 6px; color: #a9b4c5; font-size: 10.5px; }
.coefficient-marker { width: 7px; height: 7px; border-radius: 50%; display: inline-block; }
.coefficient-track { height: 7px; overflow: hidden; background: rgba(255,255,255,.065); border-radius: 5px; }
.coefficient-track i { display: block; height: 100%; border-radius: 5px; }
.coefficient-row > strong { color: #b6c1d1; font-family: 'DM Mono', monospace; font-size: 10px; text-align: right; }

.cv-row { display: grid; grid-template-columns: 46px 1fr 34px; align-items: center; gap: 8px; margin-bottom: 12px; }
.cv-row span, .cv-row strong { color: #8491a5; font-family: 'DM Mono', monospace; font-size: 10px; }
.cv-row strong { color: #bdc8d8; text-align: right; }
.cv-row > div { height: 6px; overflow: hidden; background: rgba(255,255,255,.07); border-radius: 5px; }
.cv-row i { display: block; height: 100%; background: linear-gradient(90deg, var(--blue), var(--mint)); border-radius: 5px; }
.cv-score { display: flex; align-items: baseline; gap: 9px; margin: 20px 0 20px; }
.cv-score strong { color: var(--white); font-size: 36px; letter-spacing: -.03em; }
.cv-score span { color: #718098; font-family: 'DM Mono', monospace; font-size: 10px; }
.cv-foot { display: flex; align-items: center; gap: 7px; margin-top: 20px; padding-top: 12px; border-top: 1px solid var(--line-soft); color: var(--mint); font-family: 'DM Mono', monospace; font-size: 10px; }

/* ---- About / Developer pages ---- */
.pipeline-number {
  display: grid; width: 38px; height: 38px; place-items: center; margin-bottom: 14px; border-radius: 11px; font-size: 17px;
}
.pipeline-blue { color: var(--blue); background: rgba(135,169,240,.13); }
.pipeline-peach { color: var(--peach); background: rgba(239,159,122,.13); }
.pipeline-mint { color: var(--mint); background: rgba(142,216,193,.13); }
.pipeline-lilac { color: var(--lilac); background: rgba(175,158,234,.13); }
.pipeline-index { color: #56657d; font-family: 'DM Mono', monospace; font-size: 10px; float: right; }
.pipeline-step h3 { margin: 0 0 6px; color: #e1e8f2; font-size: 13.5px; }
.pipeline-step p { margin: 0; color: #78869b; font-size: 11px; line-height: 1.7; }

.quote-mark { color: var(--mint); font-family: Georgia, serif; font-size: 26px; }
.about-bullets { display: flex; flex-wrap: wrap; gap: 10px 18px; margin-top: 12px; }
.about-bullets > div { display: inline-flex; align-items: center; gap: 6px; color: #a9b5c6; font-size: 11px; }
.snapshot-row { display: flex; align-items: center; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid var(--line-soft); font-size: 11px; }
.snapshot-row span { color: #75839a; } .snapshot-row strong { color: #c4cedd; font-family: 'DM Mono', monospace; font-size: 10.5px; }

.developer-portrait {
  display: grid; place-items: center; width: 100%; height: 160px; border-radius: 12px; position: relative;
  background: linear-gradient(145deg, #1c3454, #26313f 60%, #70525d); overflow: hidden;
}
.portrait-initials { color: rgba(255,255,255,.84); font-size: 36px; font-weight: 800; }
.portrait-status {
  position: absolute; bottom: 10px; left: 10px; display: flex; align-items: center; gap: 6px;
  padding: 5px 8px; color: #d4f2e6; background: rgba(8,17,34,.6); border: 1px solid rgba(255,255,255,.13);
  border-radius: 5px; font-family: 'DM Mono', monospace; font-size: 9px;
}
.skill-row { display: grid; grid-template-columns: 28px 1fr; align-items: center; gap: 10px; padding: 10px 11px; margin-bottom: 6px; background: rgba(255,255,255,.035); border-radius: 8px; }
.skill-row > span { color: #5f6e87; font-family: 'DM Mono', monospace; font-size: 10px; }
.skill-row strong { color: #bfc9d8; font-size: 11.5px; }
.external-link {
  display: grid; grid-template-columns: 30px 1fr; align-items: center; gap: 10px; padding: 12px;
  background: rgba(255,255,255,.035); border: 1px solid var(--line-soft); border-radius: 9px; margin-bottom: 10px;
}
.link-letter { display: grid; place-items: center; width: 28px; height: 28px; border-radius: 8px; color: var(--lilac); background: rgba(175,158,234,.11); font-size: 12px; font-weight: 700; }
.external-link strong { color: #c7d1e0; font-size: 11px; display: block; }
.external-link small { color: #738199; font-size: 9.5px; }

/* ---- Keyframes ---- */
@keyframes pulse { 0%, 100% { box-shadow: 0 0 0 3px rgba(142,216,193,.1); } 50% { box-shadow: 0 0 0 6px rgba(142,216,193,.025); } }
@keyframes orbFloat { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-5px); } }
@keyframes orbSpin { from { transform: rotate(0); } to { transform: rotate(360deg); } }
@keyframes pageEnter { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
.page-enter { animation: pageEnter .5s ease both; }

/* ---- Streamlit widget restyle to fit dark glass theme ---- */
[data-testid="stMetric"] { background: transparent; }
div[data-baseweb="select"] > div, .stNumberInput input, .stTextInput input {
  background: rgba(255,255,255,.045) !important; border: 1px solid rgba(255,255,255,.1) !important; color: var(--white) !important;
}
.stSlider [data-baseweb="slider"] { color: var(--blue); }
hr { border-color: var(--line-soft); }
</style>
"""
