"""
Direct port of src/data/mockData.ts
All constants, sample data, and the predictCharge() formula are kept
numerically identical to the original TypeScript source.
"""

# ---- Navigation ------------------------------------------------------------

NAVIGATION = [
    {"key": "home", "label": "Overview", "icon": "home"},
    {"key": "predict", "label": "Predict charges", "icon": "sparkles"},
    {"key": "analytics", "label": "Analytics", "icon": "chart"},
    {"key": "performance", "label": "Model performance", "icon": "activity"},
]

SECONDARY_NAVIGATION = [
    {"key": "about", "label": "About the project", "icon": "book"},
    {"key": "developer", "label": "Developer", "icon": "code"},
]

PAGE_TITLES = {
    "home": "Overview",
    "predict": "Predict charges",
    "analytics": "Analytics",
    "performance": "Model performance",
    "about": "About the project",
    "developer": "Developer",
}

# ---- Sample / mock datasets -------------------------------------------------

AGE_BUCKETS = [
    {"label": "18–24", "value": 19},
    {"label": "25–34", "value": 31},
    {"label": "35–44", "value": 27},
    {"label": "45–54", "value": 35},
    {"label": "55–64", "value": 42},
    {"label": "65+", "value": 18},
]

BMI_BUCKETS = [
    {"label": "Under", "value": 12},
    {"label": "Healthy", "value": 38},
    {"label": "Over", "value": 32},
    {"label": "Obese", "value": 51},
]

REGIONAL_DATA = [
    {"label": "Southwest", "value": 384},
    {"label": "Southeast", "value": 372},
    {"label": "Northwest", "value": 306},
    {"label": "Northeast", "value": 275},
]

CHARGE_TREND = [
    38, 42, 39, 46, 50, 48, 55, 58, 62, 59, 66, 70, 73, 69, 77, 81,
    76, 84, 87, 91, 89, 94, 98, 96,
]

ACTUAL_PREDICTED = [
    {"actual": 2100, "predicted": 2900},
    {"actual": 4200, "predicted": 5100},
    {"actual": 6900, "predicted": 7200},
    {"actual": 9100, "predicted": 8600},
    {"actual": 11600, "predicted": 10500},
    {"actual": 14200, "predicted": 15100},
    {"actual": 17300, "predicted": 16600},
    {"actual": 21000, "predicted": 20200},
    {"actual": 25800, "predicted": 24700},
    {"actual": 30200, "predicted": 31800},
    {"actual": 36100, "predicted": 34800},
    {"actual": 42100, "predicted": 44600},
]

COEFFICIENTS = [
    {"label": "Smoker", "value": 86, "color": "#ef9f7a"},
    {"label": "Age", "value": 42, "color": "#f0c36e"},
    {"label": "BMI", "value": 34, "color": "#86d6c0"},
    {"label": "Children", "value": 12, "color": "#86a8ef"},
    {"label": "Region", "value": 8, "color": "#a997e8"},
]

SCATTER_POINTS = [
    (12, 72), (16, 48), (19, 67), (23, 42), (27, 62), (31, 35),
    (36, 52), (41, 30), (48, 46), (56, 20), (63, 38), (72, 15),
    (82, 27), (91, 10),
]

RESIDUAL_VALUES = [-20, 12, -8, 20, -13, 7, -28, 14, 4, -9, 25, -4, 10, -18, 4, -6, 13, -12]

CV_FOLD_SCORES = [0.76, 0.81, 0.78, 0.82, 0.79]

CORRELATION_MATRIX = {
    "labels": ["Age", "BMI", "Children", "Smoker", "Charges"],
    "rows": [
        ["0.00", "0.11", "0.04", "0.03", "0.30"],
        ["0.11", "0.00", "0.02", "0.00", "0.20"],
        ["0.04", "0.02", "0.00", "0.01", "0.07"],
        ["0.03", "0.00", "0.01", "0.00", "0.79"],
        ["0.30", "0.20", "0.07", "0.79", "0.00"],
    ],
}

PIPELINE_STEPS = [
    {
        "number": "01", "title": "Collect", "tone": "blue",
        "copy": "1,337 anonymized records covering age, BMI, dependents, lifestyle, and region.",
    },
    {
        "number": "02", "title": "Prepare", "tone": "peach",
        "copy": "Categorical fields are encoded and numeric values are checked for valid ranges.",
    },
    {
        "number": "03", "title": "Learn", "tone": "mint",
        "copy": "A Linear Regression model maps the input signals to annual insurance charges.",
    },
    {
        "number": "04", "title": "Explain", "tone": "lilac",
        "copy": "Every estimate is paired with the contributing factors, not hidden behind a score.",
    },
]

DEVELOPER_SKILLS = ["Python", "Machine Learning", "Data Science", "SQL", "Git", "scikit-learn"]


# ---- Formatting / model helpers --------------------------------------------

def format_currency(value: float) -> str:
    """Mirrors formatCurrency() from mockData.ts (en-IN, INR, no decimals)."""
    return f"₹{round(value):,}"


import joblib
from pathlib import Path

_ARTIFACT_DIR = Path(__file__).resolve().parent
_MODEL_PATH = _ARTIFACT_DIR / "insurance_model.pkl"
_SCALER_PATH = _ARTIFACT_DIR / "scaler.pkl"

# Module-level cache: joblib.load() only runs once per process, since Python
# caches imported modules — Streamlit reruns the script on every interaction,
# but does not re-execute already-imported module bodies, so this is not
# reloaded from disk on every prediction.
_model = None
_scaler = None


def _load_artifacts():
    """Lazily load the trained LinearRegression model and the StandardScaler
    used during training. Loaded once and reused for the lifetime of the app."""
    global _model, _scaler
    if _model is None:
        _model = joblib.load(_MODEL_PATH)
    if _scaler is None:
        _scaler = joblib.load(_SCALER_PATH)
    return _model, _scaler


def predict_charge(age: int, gender: str, bmi: float, children: int, smoker: str, region: str) -> int:
    """
    Real model inference, replacing the old placeholder formula.

    Preprocessing mirrors the training pipeline exactly, as read directly
    from the fitted objects:
      - model.feature_names_in_ == ['age', 'is_female', 'bmi', 'children',
        'is_smoker', 'region_southeast', 'bmi_category_Obese']
      - scaler.feature_names_in_ == ['age', 'bmi', 'children']  (only these
        three numeric columns were standardized; the rest are raw 0/1 flags)
    """
    model, scaler = _load_artifacts()

    # Scale age/bmi/children with the SAME StandardScaler fit during training.
    # scaler.transform expects a 2D array in the column order it was fit on.
    age_scaled, bmi_scaled, children_scaled = scaler.transform([[age, bmi, children]])[0]

    # Recreate the one-hot / binary columns the model was trained on.
    is_female = 1 if gender == "Female" else 0
    is_smoker = 1 if smoker == "Yes" else 0
    region_southeast = 1 if region == "Southeast" else 0
    bmi_category_obese = 1 if bmi >= 30 else 0  # standard clinical BMI >= 30 cutoff

    # Column order MUST match model.feature_names_in_ exactly.
    features = [[
        age_scaled,
        is_female,
        bmi_scaled,
        children_scaled,
        is_smoker,
        region_southeast,
        bmi_category_obese,
    ]]

    prediction = model.predict(features)[0]
    return max(round(prediction), 0)
