import streamlit as st
import plotly.graph_objects as go

from components import page_title, metric_card, chart_header, surface_open, surface_close, tag
from data import ACTUAL_PREDICTED, RESIDUAL_VALUES, CV_FOLD_SCORES, COEFFICIENTS

METRICS = {
    "R² score": dict(value="0.804", trend="+2.1%", trend_label="vs. baseline", accent="mint",
                      helper="How much variation the model explains",
                      callout="The model explains 80.4% of charge variation in held-out data."),
    "Adjusted R²": dict(value="0.799", trend="Strong", trend_label="complexity adjusted", accent="blue",
                         helper="R² adjusted for input count",
                         callout="Select a metric card to see its role in the evaluation."),
    "MAE": dict(value="₹4,295", trend="Low", trend_label="average error", accent="peach",
                helper="Mean absolute error",
                callout="Select a metric card to see its role in the evaluation."),
    "RMSE": dict(value="₹6,000", trend="Stable", trend_label="penalizes outliers", accent="lilac",
                 helper="Root mean square error",
                 callout="Select a metric card to see its role in the evaluation."),
}


def _actual_predicted_chart():
    actual = [d["actual"] for d in ACTUAL_PREDICTED]
    predicted = [d["predicted"] for d in ACTUAL_PREDICTED]
    max_v = 45000
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, max_v], y=[0, max_v], mode="lines",
                              line=dict(color="rgba(142,216,193,.55)", dash="dash", width=1.4),
                              name="Perfect fit"))
    fig.add_trace(go.Scatter(x=actual, y=predicted, mode="lines+markers",
                              line=dict(color="#87a9f0", width=2.2),
                              marker=dict(size=7, color="#87a9f0", line=dict(color="#17233a", width=2)),
                              name="Predicted charges"))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=45, r=10, t=10, b=40), height=260, showlegend=False,
        xaxis=dict(title="Actual charges", showgrid=True, gridcolor="rgba(255,255,255,.05)",
                    color="#66758c", tickfont=dict(size=9)),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,.05)", color="#66758c", tickfont=dict(size=9)),
    )
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})


def _residual_chart():
    fig = go.Figure(
        go.Bar(x=list(range(len(RESIDUAL_VALUES))), y=RESIDUAL_VALUES,
               marker_color=["#87a9f0" if v >= 0 else "#ef9f7a" for v in RESIDUAL_VALUES])
    )
    fig.add_hline(y=0, line_dash="dash", line_color="rgba(142,216,193,.48)")
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=10, b=30), height=220, showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(showgrid=False, visible=False),
    )
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})
    st.markdown(
        '<div style="display:flex; justify-content:space-between; color:#68788e; font-family:\'DM Mono\',monospace; font-size:9px; margin-top:-14px;">'
        '<span>Under-predicted</span><span>0 error</span><span>Over-predicted</span></div>',
        unsafe_allow_html=True,
    )


def render():
    st.markdown('<div class="page-enter">', unsafe_allow_html=True)

    if "selected_metric" not in st.session_state:
        st.session_state.selected_metric = "R² score"

    page_title(
        "Model performance",
        "A model you can inspect.",
        "Not just a score. A clear view into how this model behaves, where it is strong, and where it can improve.",
        action_html=tag("Evaluation complete", "mint", True),
    )

    cols = st.columns(4)
    for col, (name, m) in zip(cols, METRICS.items()):
        with col:
            if st.button(name, key=f"metric_btn_{name}", width="stretch"):
                st.session_state.selected_metric = name
                st.rerun()
            metric_card(name, m["value"], m["trend"], m["trend_label"], accent=m["accent"], helper=m["helper"])

    sel = METRICS[st.session_state.selected_metric]
    st.markdown(
        f"""
        <div class="performance-callout">
          <div class="callout-icon">🎯</div>
          <div><strong>{st.session_state.selected_metric} selected</strong><span>{sel['callout']}</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.28, 0.72], gap="medium")
    with col1:
        surface_open("")
        chart_header("Actual vs. predicted", "Held-out test set · 268 records")
        _actual_predicted_chart()
        st.markdown(
            '<div class="chart-insight">✨ Points cluster around the ideal fit, with higher variance at the upper end.</div>',
            unsafe_allow_html=True,
        )
        surface_close()

    with col2:
        surface_open("")
        chart_header("Cross-validation", "5-fold validation scores")
        mean_score = sum(CV_FOLD_SCORES) / len(CV_FOLD_SCORES)
        st.markdown(
            f'<div class="cv-score"><strong>{mean_score:.2f}</strong><span>mean score</span></div>',
            unsafe_allow_html=True,
        )
        rows_html = ""
        for i, val in enumerate(CV_FOLD_SCORES):
            rows_html += f"""
            <div class="cv-row"><span>Fold {i + 1}</span><div><i style="width:{val * 100}%;"></i></div><strong>{val:.2f}</strong></div>
            """
        st.markdown(rows_html, unsafe_allow_html=True)
        st.markdown('<div class="cv-foot">✓ Consistent across every fold</div>', unsafe_allow_html=True)
        surface_close()

    st.write("")

    col3, col4 = st.columns([0.95, 1.05], gap="medium")
    with col3:
        surface_open("")
        chart_header("Residual analysis", "Error distribution across predictions")
        _residual_chart()
        st.markdown(
            '<div class="chart-insight chart-insight-warm">📉 Residuals are centered around zero, a healthy sign of low systematic bias.</div>',
            unsafe_allow_html=True,
        )
        surface_close()

    with col4:
        surface_open("")
        chart_header("Coefficient importance", "Relative influence on charge")
        rows_html = ""
        for c in COEFFICIENTS:
            rows_html += f"""
            <div class="coefficient-row">
              <div class="coefficient-name"><span class="coefficient-marker" style="background:{c['color']};"></span>{c['label']}</div>
              <div class="coefficient-track"><i style="width:{c['value']}%; background:{c['color']};"></i></div>
              <strong>{c['value']}%</strong>
            </div>
            """
        st.markdown(f'<div style="margin-top:20px;">{rows_html}</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="cv-foot">📈 Smoker status is the strongest predictor in this model.</div>',
            unsafe_allow_html=True,
        )
        surface_close()

    st.markdown(
        '<div class="model-footnote">Evaluation metrics are calculated on a held-out test set and should be interpreted alongside the domain context.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
