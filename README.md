# Covera — Insurance Charge Predictor (Streamlit port)

A migration of the original React + TypeScript "Covera" portfolio app to
Streamlit — same pages, same design tokens, same (fake, formula-based)
prediction logic, now running as a pure Python/Streamlit app.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Files

- `app.py` — app shell: sidebar nav, topbar, session-state page router
- `theme.py` — global CSS (colors, fonts, keyframe animations)
- `components.py` — reusable UI helpers (MetricCard, Tag, PageTitle, ChartHeader...)
- `data.py` — ported mock data + the `predict_charge()` formula
- `pages_home.py`, `pages_predict.py`, `pages_analytics.py`,
  `pages_performance.py`, `pages_about.py`, `pages_developer.py` — one file per page

## Prediction model

`predict_charge()` in `data.py` now loads your real trained artifacts
(`insurance_model.pkl`, `scaler.pkl`) via `joblib` instead of using a
placeholder formula. Keep both `.pkl` files in the same folder as `data.py`.

Preprocessing was reverse-engineered directly from the fitted objects:
- `age`, `bmi`, `children` are standardized with the same `StandardScaler`
  used at training time.
- `gender`, `smoker`, `region`, and BMI category are turned into the exact
  binary columns the model expects: `is_female`, `is_smoker`,
  `region_southeast`, `bmi_category_Obese` (obese = BMI ≥ 30).
- Final feature order matches `model.feature_names_in_` exactly:
  `['age', 'is_female', 'bmi', 'children', 'is_smoker', 'region_southeast', 'bmi_category_Obese']`.

Note: the pickles were saved with scikit-learn 1.9.0; this environment has
1.8.0, which triggers a harmless `InconsistentVersionWarning` on load. For a
production deployment, pin `scikit-learn==1.9.0` in `requirements.txt` to
silence it.

## Notes on the port

- All hand-drawn SVG/div charts from the React version were rebuilt in Plotly
  (bar charts, scatter, heatmap, line charts), matching the original color
  palette with transparent backgrounds so they sit inside the glass "surface" cards.
- The dark/light theme toggle in the sidebar is visual only — Streamlit
  doesn't support live theme swapping without a full rerun/config change,
  and the original toggle didn't actually change page content either.
- Routing uses `st.session_state`, matching the original app's behavior
  (which also had no real URL-based routing, just in-memory page state).
- The `predict_charge()` formula is a direct, numerically identical port
  of the original `predictCharge()` from `mockData.ts`.
