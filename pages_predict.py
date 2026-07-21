import streamlit as st

from components import page_title, section_label, surface_open, surface_close, tag
from data import predict_charge, format_currency


def _risk_tier(inputs, result):
    if result is None:
        return "low"
    if inputs["smoker"] == "Yes" or inputs["bmi"] >= 30 or inputs["age"] >= 55:
        return "high"
    if inputs["bmi"] >= 25 or inputs["age"] >= 40 or inputs["children"] >= 3:
        return "medium"
    return "low"


RISK_COPY = {
    "low": ("Lower risk profile", "mint", "Your profile sits below the model's higher-cost signals."),
    "medium": ("Moderate risk profile", "yellow", "A few inputs are contributing to a moderately higher estimate."),
    "high": ("Higher risk profile", "peach", "One or more strong cost drivers are influencing this estimate."),
}


def render():
    st.markdown('<div class="page-enter">', unsafe_allow_html=True)

    page_title(
        "Prediction workspace",
        "What could your coverage cost?",
        "Adjust the inputs below to generate a transparent, model-backed estimate.",
        action_html=tag("Model online", "mint", True),
    )

    if "predict_result" not in st.session_state:
        st.session_state.predict_result = None

    form_col, result_col = st.columns([1.08, 0.92], gap="large")

    with form_col:
        surface_open("")
        st.markdown(
            """
            <div style="display:flex; align-items:flex-start; justify-content:space-between;
                        padding-bottom:18px; border-bottom:1px solid var(--line-soft); margin-bottom:18px;">
              <div><p class="section-label">Profile inputs</p>
                   <h2 style="margin:0; color:var(--white); font-size:18px; letter-spacing:-.02em;">Tell us about the person</h2></div>
              <span style="color:var(--blue); font-family:'DM Mono',monospace; font-size:11px;">01 <span style="color:#61718a;">/ 01</span></span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("prediction_form"):
            c1, c2 = st.columns(2)
            with c1:
                age = st.number_input("Age (years)", min_value=18, max_value=100, value=32, help="Age is used as a continuous variable in the model.")
            with c2:
                gender = st.selectbox("Gender", ["Female", "Male", "Other"])

            c3, c4 = st.columns(2)
            with c3:
                bmi = st.number_input("BMI (kg/m²)", min_value=10.0, max_value=70.0, value=27.4, step=0.1, help="Body Mass Index, a ratio of weight to height.")
            with c4:
                children = st.number_input("Children", min_value=0, max_value=10, value=1, help="Dependents under coverage")

            smoker = st.radio("Does the person smoke?", ["No", "Yes"], horizontal=True)
            region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

            st.markdown(
                '<div style="display:flex; align-items:center; gap:7px; color:#718098; font-size:10.5px; margin:12px 0;">'
                '🛡️ Your inputs stay in this session</div>',
                unsafe_allow_html=True,
            )
            submitted = st.form_submit_button("Calculate estimate →")

        error = ""
        if submitted:
            if age < 18 or age > 100:
                error = "Age must be between 18 and 100."
            elif bmi < 10 or bmi > 70:
                error = "BMI must be between 10 and 70."
            elif children < 0 or children > 10:
                error = "Children must be between 0 and 10."
            else:
                st.session_state.predict_result = predict_charge(int(age), gender, float(bmi), int(children), smoker, region)
                st.session_state.predict_inputs = dict(age=int(age), gender=gender, bmi=float(bmi),
                                                        children=int(children), smoker=smoker, region=region)

        if error:
            st.markdown(f'<p style="color:var(--peach); font-size:11px;">{error}</p>', unsafe_allow_html=True)

        surface_close()

    with result_col:
        result = st.session_state.predict_result
        inputs = st.session_state.get("predict_inputs", {})

        surface_open("")
        if not result:
            st.markdown(
                """
                <div class="result-empty">
                  <div class="result-orbit">✨</div>
                  <p class="section-label" style="color:var(--mint);">Your estimate</p>
                  <h2>A clearer view is one click away.</h2>
                  <p>Complete the profile and we'll translate the model's output into a simple estimate with context.</p>
                  <span class="result-note">Powered by Linear Regression</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            risk = _risk_tier(inputs, result)
            risk_label, risk_tone, risk_copy = RISK_COPY[risk]

            st.markdown(
                f"""
                <div style="display:flex; align-items:flex-start; justify-content:space-between;">
                  <div><p class="section-label">Estimated annual charge</p>
                       <span style="color:#7586a0; font-family:'DM Mono',monospace; font-size:9px;">Generated just now</span></div>
                  {tag(risk_label, risk_tone, True)}
                </div>
                <div class="result-amount">{format_currency(result)}</div>
                <div class="result-range">
                  <div class="result-range-labels"><span>Expected range</span>
                    <strong>{format_currency(max(result - 4100, 0))} - {format_currency(result + 4100)}</strong></div>
                  <div class="range-track"><span class="range-fill" style="width:62%; margin-left:18%; display:block;"></span></div>
                  <div class="range-scale"><span>Lower</span><span>Model estimate</span><span>Higher</span></div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            smoker_msg = ("Smoking status is the strongest upward signal." if inputs.get("smoker") == "Yes"
                          else "Non-smoking status helps keep this estimate lower.")
            smoker_strength = "High impact" if inputs.get("smoker") == "Yes" else "Positive"
            bmi_msg = ("BMI is contributing to a higher estimate." if inputs.get("bmi", 0) >= 25
                       else "BMI is within a lower-impact range.")
            bmi_strength = "Medium" if inputs.get("bmi", 0) >= 25 else "Low impact"
            children_n = inputs.get("children", 0)
            children_word = "are" if children_n == 1 else "are"

            st.markdown(
                f"""
                <div style="padding:18px 0 4px;">
                  <div style="display:flex; align-items:center; justify-content:space-between;">
                    <h3 style="margin:0; color:#dfe6f1; font-size:12px;">What shaped this estimate</h3>
                    <span style="color:#7485a0; font-size:9px;">Model confidence <strong style="color:var(--mint);">80.4%</strong></span>
                  </div>
                  <div class="signal-list">
                    <div class="signal-row"><span class="signal-dot signal-peach"></span><span>{smoker_msg}</span><strong class="signal-strong">{smoker_strength}</strong></div>
                    <div class="signal-row"><span class="signal-dot signal-yellow"></span><span>{bmi_msg}</span><strong class="signal-strong">{bmi_strength}</strong></div>
                    <div class="signal-row"><span class="signal-dot signal-blue"></span><span>Age and {children_n} dependent{'s' if children_n != 1 else ''} {children_word} included in the estimate.</span><strong class="signal-strong">Included</strong></div>
                  </div>
                </div>
                <div class="recommendation">
                  <div class="recommendation-icon">✨</div>
                  <div><strong>One useful next step</strong>
                    <p>{risk_copy} Compare this scenario with a non-smoking profile to see the model's sensitivity.</p></div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Run another scenario →", key="predict_reset"):
                st.session_state.predict_result = None
                st.rerun()

        surface_close()

    st.markdown(
        '<div class="disclaimer">✓ This is an educational estimate based on a trained model, not financial or medical advice.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
