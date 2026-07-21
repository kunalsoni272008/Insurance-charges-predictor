import streamlit as st
import plotly.graph_objects as go

from components import page_title, metric_card, chart_header, surface_open, surface_close
from data import AGE_BUCKETS, BMI_BUCKETS, REGIONAL_DATA, SCATTER_POINTS, CORRELATION_MATRIX


def _bar_chart(data, color, suffix=""):
    labels = [d["label"] for d in data]
    values = [d["value"] for d in data]
    fig = go.Figure(
        go.Bar(x=labels, y=values, marker_color=color, marker_line_width=0,
               text=[f"{v}{suffix}" for v in values], textposition="outside",
               textfont=dict(color="#96a5bd", size=10))
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=24, b=10), height=220, showlegend=False,
        xaxis=dict(showgrid=False, color="#6e7d94", tickfont=dict(size=10)),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,.06)", visible=False),
    )
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})


def _scatter_chart():
    xs = [p[0] for p in SCATTER_POINTS]
    ys = [100 - p[1] for p in SCATTER_POINTS]  # invert so "up" is higher charge
    colors = ["#ef9f7a" if (i % 4 == 0 or i % 5 == 0) else "#87a9f0" for i in range(len(SCATTER_POINTS))]
    fig = go.Figure(
        go.Scatter(x=xs, y=ys, mode="markers",
                    marker=dict(size=9, color=colors, line=dict(color="#17233a", width=2)))
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=40, r=10, t=10, b=30), height=220,
        xaxis=dict(title="Age", showgrid=True, gridcolor="rgba(255,255,255,.05)",
                    color="#65748b", tickfont=dict(size=9)),
        yaxis=dict(title="Charges", showgrid=True, gridcolor="rgba(255,255,255,.05)",
                    color="#65748b", tickfont=dict(size=9),
                    tickvals=[0, 50, 100], ticktext=["₹50k", "₹25k", "₹0"]),
    )
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})


def _heatmap():
    labels = CORRELATION_MATRIX["labels"]
    rows = [[float(v) for v in row] for row in CORRELATION_MATRIX["rows"]]
    fig = go.Figure(
        go.Heatmap(
            z=rows, x=labels, y=labels,
            colorscale=[[0, "rgba(135,169,240,0.03)"], [1, "rgba(135,169,240,0.95)"]],
            showscale=False,
            text=[[f"{v:.2f}" for v in row] for row in rows],
            texttemplate="%{text}",
            textfont=dict(size=10, color="#d6e0ef"),
        )
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=10, r=10, t=10, b=10), height=240,
        xaxis=dict(side="top", color="#718098", tickfont=dict(size=9)),
        yaxis=dict(autorange="reversed", color="#718098", tickfont=dict(size=9)),
    )
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})


def render():
    st.markdown('<div class="page-enter">', unsafe_allow_html=True)

    if "analytics_range" not in st.session_state:
        st.session_state.analytics_range = "Last 30 days"

    page_title(
        "Analytics dashboard",
        "See the signal in the data.",
        "A live view of the training set, patterns, and distributions behind the estimate.",
    )

    st.markdown(
        """
        <div style="display:flex; align-items:center; justify-content:space-between; margin:-8px 0 16px;">
          <div style="display:flex; align-items:center; gap:9px; color:#75849c; font-family:'DM Mono',monospace; font-size:10px;">
            <span class="live-pulse"></span> Dataset refreshed 8 minutes ago
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    range_choice = st.radio("Range", ["Last 7 days", "Last 30 days", "All time"],
                             horizontal=True, label_visibility="collapsed",
                             index=["Last 7 days", "Last 30 days", "All time"].index(st.session_state.analytics_range))
    st.session_state.analytics_range = range_choice

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card("Average charges", "₹13,270", "+6.2%", "vs. prior period", "📈", "blue")
    with c2:
        metric_card("Average BMI", "30.66", "+0.8%", "population average", "⚖️", "mint")
    with c3:
        metric_card("Average age", "39.2 yrs", "Stable", "population average", "🎂", "lilac")
    with c4:
        metric_card("Highest charge", "₹63,770", "Top 1%", "observed record", "🔝", "peach")

    st.write("")

    col1, col2, col3 = st.columns([1.05, 1.05, 0.9], gap="medium")
    with col1:
        surface_open("")
        chart_header("Age distribution", "Records by age bracket")
        _bar_chart(AGE_BUCKETS, "#87a9f0")
        st.markdown(
            '<div style="display:flex; justify-content:space-between; color:#74839b; font-family:\'DM Mono\',monospace; font-size:9px;">'
            '<span>● Patient records</span><strong>1,337 total</strong></div>',
            unsafe_allow_html=True,
        )
        surface_close()

    with col2:
        surface_open("")
        chart_header("BMI distribution", "Population health profile")
        _bar_chart(BMI_BUCKETS, "#8ed8c1", suffix="%")
        st.markdown(
            """
            <div class="legend-row">
              <span><i class="legend-dot legend-blue"></i>Under 18.5</span>
              <span><i class="legend-dot legend-mint"></i>18.5–24.9</span>
              <span><i class="legend-dot legend-yellow"></i>25–29.9</span>
              <span><i class="legend-dot legend-peach"></i>30+</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        surface_close()

    with col3:
        surface_open("")
        chart_header("Regional mix", "Distribution across the dataset")
        fill_colors = ["#87a9f0", "#8ed8c1", "#ef9f7a", "#af9eea"]
        rows_html = ""
        for i, item in enumerate(REGIONAL_DATA):
            width = (item["value"] / 400) * 100
            rows_html += f"""
            <div style="display:grid; grid-template-columns:66px 1fr 34px; align-items:center; gap:10px; margin-bottom:14px;">
              <span style="color:#909db1; font-size:10px;">{item['label']}</span>
              <div style="height:7px; background:rgba(255,255,255,.07); border-radius:5px; overflow:hidden;">
                <div style="width:{width}%; height:100%; background:{fill_colors[i]}; border-radius:5px;"></div>
              </div>
              <strong style="color:#bac5d5; font-family:'DM Mono',monospace; font-size:9px; text-align:right;">{item['value']}</strong>
            </div>
            """
        st.markdown(f'<div style="margin-top:16px;">{rows_html}</div>', unsafe_allow_html=True)
        st.markdown(
            '<div style="display:flex; justify-content:space-between; margin-top:16px; padding-top:12px; '
            'border-top:1px solid var(--line-soft); color:#74839b; font-family:\'DM Mono\',monospace; font-size:9px;">'
            '<span>Largest cohort</span><strong style="color:var(--mint);">Southeast ↗</strong></div>',
            unsafe_allow_html=True,
        )
        surface_close()

    st.write("")

    col_a, col_b = st.columns(2, gap="medium")
    with col_a:
        surface_open("")
        chart_header("Age vs. charges", "Smoker and non-smoker observations")
        st.markdown(
            '<div class="legend-row"><span><i class="legend-dot legend-blue"></i>Non-smoker</span>'
            '<span><i class="legend-dot legend-peach"></i>Smoker</span></div>',
            unsafe_allow_html=True,
        )
        _scatter_chart()
        surface_close()

    with col_b:
        surface_open("")
        chart_header("Correlation matrix", "Strength of relationships between variables")
        _heatmap()
        st.markdown(
            '<div style="display:flex; align-items:center; gap:7px; margin-top:14px; color:#7d8ca2; font-size:10px;">'
            '📈 Smoker status shows the strongest relationship with charges <strong style="color:var(--mint); font-family:\'DM Mono\',monospace;">0.79</strong></div>',
            unsafe_allow_html=True,
        )
        surface_close()

    st.markdown(
        f'<div class="analytics-note">📊 Showing aggregated data from <strong>{range_choice.lower()}</strong>. Hover chart elements for details.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
