import streamlit as st

from components import page_title, section_label, surface_open, surface_close, tag
from data import PIPELINE_STEPS

PIPELINE_ICONS = {"01": "🗄️", "02": "🎚️", "03": "🔬", "04": "✨"}


def render():
    st.markdown('<div class="page-enter">', unsafe_allow_html=True)

    page_title(
        "About the project",
        "Designed for understanding.",
        "A portfolio project exploring how machine learning can make insurance pricing feel more human.",
        action_html=tag("Project brief · v1.0", "blue"),
    )

    col1, col2 = st.columns([1.3, 0.7], gap="large")
    with col1:
        section_label("The problem")
        st.markdown(
            '<h2 style="margin:0; color:var(--white); font-size:clamp(22px,3vw,34px); letter-spacing:-.03em; line-height:1.15;">'
            "People shouldn't need a data science degree to understand a price.</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="color:var(--muted); font-size:12.5px; line-height:1.8; margin:16px 0;">'
            "Medical insurance costs are shaped by multiple variables, but the reasoning often remains invisible. "
            "This project uses an interpretable model to make that reasoning visible and approachable.</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style="display:flex; align-items:center; gap:10px; color:#9eabbf; font-family:\'DM Mono\',monospace; font-size:10px;">'
            '<span class="quote-mark">"</span><span>Clarity is a feature, not a side effect.</span></div>',
            unsafe_allow_html=True,
        )

    with col2:
        surface_open("")
        st.markdown(
            """
            <div style="display:flex; align-items:center; justify-content:space-between; padding-bottom:12px;
                        color:#bcc7d7; font-size:11px; border-bottom:1px solid var(--line-soft); margin-bottom:6px;">
              <span>Project snapshot</span><span>🔀</span>
            </div>
            <div class="snapshot-row"><span>Dataset</span><strong>Medical Cost Personal</strong></div>
            <div class="snapshot-row"><span>Rows</span><strong>1,337</strong></div>
            <div class="snapshot-row"><span>Target</span><strong>Annual charges</strong></div>
            <div class="snapshot-row"><span>Model family</span><strong>Supervised regression</strong></div>
            <div class="snapshot-row" style="border-bottom:none;"><span>Validation</span>
              <strong style="color:var(--mint); display:flex; align-items:center; gap:6px;">
                <span class="status-dot status-dot-green"></span>Held-out test set</strong></div>
            """,
            unsafe_allow_html=True,
        )
        surface_close()

    st.write("")

    surface_open("")
    st.markdown(
        """
        <div style="display:flex; align-items:flex-end; justify-content:space-between; padding-bottom:18px;
                    border-bottom:1px solid var(--line-soft);">
          <div><p class="section-label">Machine learning pipeline</p>
               <h2 style="margin:0; color:var(--white); font-size:20px; letter-spacing:-.02em;">Four steps from raw data to a useful answer.</h2></div>
          <span style="color:#76859c; font-family:'DM Mono',monospace; font-size:10px;">Built to be inspectable</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns(4)
    for col, step in zip(cols, PIPELINE_STEPS):
        with col:
            st.markdown(
                f"""
                <div class="pipeline-step" style="margin-top:20px;">
                  <span class="pipeline-index">{step['number']}</span>
                  <div class="pipeline-number pipeline-{step['tone']}">{PIPELINE_ICONS[step['number']]}</div>
                  <h3>{step['title']}</h3>
                  <p>{step['copy']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
    surface_close()

    st.write("")

    col3, col4 = st.columns(2, gap="medium")
    with col3:
        surface_open("")
        section_label("Model choice")
        st.markdown(
            '<h2 style="margin:0; color:var(--white); font-size:21px; letter-spacing:-.02em;">Simple enough to trust.</h2>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="color:var(--muted); font-size:12px; line-height:1.75; margin:12px 0 16px;">'
            "Linear Regression was selected for its interpretability and strong baseline performance. It offers a "
            "direct way to discuss how each input moves the estimate, which is valuable in a high-context domain like insurance.</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="about-bullets">
              <div>✓ Clear coefficient direction</div>
              <div>✓ Fast, lightweight inference</div>
              <div>✓ Easy to evaluate and improve</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        surface_close()

    with col4:
        surface_open("")
        st.markdown('<div style="font-size:20px;">🧱</div>', unsafe_allow_html=True)
        section_label("Next horizon")
        st.markdown(
            '<h3 style="margin:0; color:var(--white); font-size:19px; letter-spacing:-.02em;">Where this could go next</h3>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="color:#8794aa; font-size:11px; line-height:1.7; margin:12px 0 0;">'
            "Explore non-linear models, add confidence intervals, fairness checks, and connect the output to real policy design.</p>",
            unsafe_allow_html=True,
        )
        surface_close()

    st.write("")
    fc1, fc2 = st.columns([1, 3])
    with fc1:
        st.button("Read the methodology →", key="about_methodology")
    with fc2:
        st.markdown(
            '<div style="display:flex; align-items:center; height:42px; color:#66768e; font-family:\'DM Mono\',monospace; font-size:10px;">'
            'Open-source thinking, thoughtfully packaged.</div>',
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)
