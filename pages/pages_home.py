import streamlit as st
import plotly.graph_objects as go

from components import metric_card, section_label, chart_header, surface_open, surface_close, brand_mark, tag
from data import CHARGE_TREND, format_currency


def _trend_chart():
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            y=CHARGE_TREND,
            mode="lines",
            line=dict(color="#8ed8c1", width=2.4, shape="spline"),
            fill="tozeroy",
            fillcolor="rgba(142,216,193,0.12)",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[len(CHARGE_TREND) - 1],
            y=[CHARGE_TREND[-1]],
            mode="markers",
            marker=dict(color="#8ed8c1", size=9, line=dict(color="#17233a", width=3)),
        )
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=6, b=0),
        height=140,
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
    )
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})


def render():
    st.markdown('<div class="page-enter">', unsafe_allow_html=True)

    # ---- Hero ----
    left, right = st.columns([1.05, 0.95], gap="large")
    with left:
        st.markdown(
            f"""
            <div class="home-hero" style="padding-right: 20px;">
              <div class="hero-brand-line">{brand_mark()}<span>Covera intelligence</span>{tag("Model live", "mint", True)}</div>
              <div class="hero-copy">
                <h1>Predict tomorrow&apos;s <em class="hl">cost,</em> today.</h1>
                <p class="hero-description">A transparent, data-led view of medical insurance charges. Explore the signal behind every estimate.</p>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        b1, b2 = st.columns([1, 1.4])
        with b1:
            if st.button("Run a prediction →", key="home_predict_cta"):
                st.session_state.page = "predict"
                st.rerun()
        with b2:
            st.markdown('<div class="play-link">▶ See how it works</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="hero-trust">🛡️ Built with a transparent Linear Regression model</div>',
            unsafe_allow_html=True,
        )

    with right:
        surface_open("home-hero")
        st.markdown(
            f"""
            <div style="display:flex; align-items:center; justify-content:space-between; font-family:'DM Mono',monospace; font-size:10px; color:#a4b2c8;">
              <span><span class="live-pulse"></span> Prediction engine</span>
              <span style="color:#63728b;">Updated just now</span>
            </div>
            <div style="margin-top:28px; display:flex; align-items:flex-end; justify-content:space-between;">
              <div>
                <span style="color:#8292ac; font-size:10.5px;">Average predicted charge</span><br/>
                <strong style="color:var(--white); font-size:24px; letter-spacing:-.03em;">{format_currency(13240)}</strong>
              </div>
              <span style="color:var(--mint); font-family:'DM Mono',monospace; font-size:10px;">↗ 12.8%</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        _trend_chart()
        st.markdown(
            """<div style="display:flex; justify-content:space-between; color:#62718a; font-family:'DM Mono',monospace; font-size:9px;">
            <span>Jan</span><span>Mar</span><span>May</span><span>Jul</span><span>Now</span></div>""",
            unsafe_allow_html=True,
        )
        surface_close()

    st.write("")

    # ---- Stats row ----
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Dataset", "1,337", "+8.4%", "records processed", "📊", "blue",
                     "Insurance dataset rows used to train the model")
    with c2:
        metric_card("Model", "Linear regression", "Stable", "production baseline", "🧩", "lilac",
                     "Interpretable regression model")
    with c3:
        metric_card("R² score", "80.4%", "+2.1%", "vs. last run", "🎯", "mint", "Coefficient of determination")
    with c4:
        metric_card("Inference", "Real-time", "42ms", "median response", "⚡", "peach", "Average prediction latency")

    st.write("")

    # ---- Lower grid: narrative + workflow ----
    col_a, col_b = st.columns([1, 1], gap="medium")
    with col_a:
        surface_open()
        section_label("Why Covera")
        st.markdown(
            '<h2 style="margin:0; color:var(--white); font-size:24px; letter-spacing:-.03em;">'
            'Make the invisible <em class="hl">legible.</em></h2>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="color:var(--muted); font-size:12.5px; line-height:1.75; margin:14px 0 18px;">'
            'Insurance pricing can feel opaque. Covera turns the key drivers of a charge into a clear, '
            'useful starting point for better conversations.</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="feature-list">
              <div><span class="feature-check">✓</span><span>Instant estimates from six simple inputs</span></div>
              <div><span class="feature-check">✓</span><span>Explanations, not just a number</span></div>
              <div><span class="feature-check">✓</span><span>Auditable metrics for every model run</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Explore the prediction model →", key="home_explore_cta"):
            st.session_state.page = "predict"
            st.rerun()
        surface_close()

    with col_b:
        surface_open()
        chart_header("From input to insight", "A simple, explainable pipeline")
        st.markdown(
            """
            <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-top:20px;">
              <div class="workflow-step"><div class="workflow-icon workflow-icon-blue">01</div>
                <div><strong>Describe</strong><span>Share a few details</span></div></div>
              <div class="workflow-step"><div class="workflow-icon workflow-icon-peach">02</div>
                <div><strong>Calculate</strong><span>Model finds the signal</span></div></div>
              <div class="workflow-step"><div class="workflow-icon workflow-icon-mint">03</div>
                <div><strong>Understand</strong><span>See what shaped it</span></div></div>
            </div>
            <div class="workflow-foot">⚡ Average time to insight <strong>under 1 second</strong></div>
            """,
            unsafe_allow_html=True,
        )
        surface_close()

    # ---- Tech strip ----
    st.markdown(
        """
        <div class="tech-strip">
          <div><span class="tech-kicker">Under the hood</span> <strong>Small model. Clear signal.</strong></div>
          <div class="tech-items"><span>Python</span><span>scikit-learn</span><span>pandas</span><span>Plotly</span><span>Streamlit</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)
