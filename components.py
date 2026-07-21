"""
Python equivalents of src/components/UI.tsx.
Each function renders a styled HTML snippet via st.markdown, matching
the original React component's markup/classes as closely as possible.
"""

import streamlit as st


def brand_mark():
    return """<div class="brand-mark"><span></span><span></span><span></span></div>"""


def tag(text: str, tone: str = "neutral", live_dot: bool = False) -> str:
    dot = '<span class="tag-live-dot"></span>' if live_dot else ""
    return f'<span class="tag tag-{tone}">{dot}{text}</span>'


def section_label(text: str):
    st.markdown(f'<p class="section-label">{text}</p>', unsafe_allow_html=True)


def page_title(eyebrow: str, title: str, description: str, action_html: str = ""):
    st.markdown(
        f"""
        <div style="display:flex; align-items:flex-end; justify-content:space-between; gap:24px; margin-bottom:28px;">
          <div>
            <p class="eyebrow">{eyebrow}</p>
            <h1 class="page-title">{title}</h1>
            <p class="page-description">{description}</p>
          </div>
          <div>{action_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def metric_card(label: str, value: str, trend: str = "", trend_label: str = "",
                 icon: str = "", accent: str = "blue", helper: str = ""):
    positive = trend.startswith("+") if trend else None
    trend_html = ""
    if trend or trend_label:
        arrow = "↑" if positive else ("↓" if positive is False else "")
        trend_class = "trend-up" if positive else ("trend-down" if positive is False else "")
        trend_span = f'<span class="{trend_class}">{arrow} {trend}</span>' if trend else ""
        label_span = f"<span>{trend_label}</span>" if trend_label else ""
        trend_html = f'<div class="metric-meta">{trend_span}{label_span}</div>'

    icon_html = f'<span class="metric-icon">{icon}</span>' if icon else ""

    st.markdown(
        f"""
        <div class="metric-card accent-{accent}" title="{helper}">
          <div class="metric-card-top">
            <span class="metric-label">{label}</span>
            {icon_html}
          </div>
          <div class="metric-value">{value}</div>
          {trend_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def chart_header(title: str, subtitle: str = ""):
    sub = f'<p class="chart-header-sub">{subtitle}</p>' if subtitle else ""
    st.markdown(
        f"""
        <div style="display:flex; align-items:flex-start; justify-content:space-between; margin-bottom:6px;">
          <div><h3 class="chart-header-title">{title}</h3>{sub}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def surface_open(extra_class: str = ""):
    st.markdown(f'<div class="surface {extra_class}">', unsafe_allow_html=True)


def surface_close():
    st.markdown("</div>", unsafe_allow_html=True)


PLOTLY_LAYOUT_BASE = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Mono, monospace", color="#8ea0be", size=10),
    margin=dict(l=36, r=16, t=10, b=36),
    showlegend=False,
)
