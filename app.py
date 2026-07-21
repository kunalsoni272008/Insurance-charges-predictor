import streamlit as st

from theme import GLOBAL_CSS
from components import brand_mark
from data import NAVIGATION, SECONDARY_NAVIGATION, PAGE_TITLES

st.set_page_config(page_title="Covera — Insurance Charge Predictor", page_icon="✨", layout="wide")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ---- Session state ----------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "is_dark" not in st.session_state:
    st.session_state.is_dark = True


def navigate(page_key: str):
    st.session_state.page = page_key


# ---- Sidebar -----------------------------------------------------------------
with st.sidebar:
    st.markdown(
        f"""
        <div class="brand-lockup">{brand_mark()}<span class="brand-wordmark">Covera</span></div>
        <div class="workspace-switcher">
          <div class="workspace-avatar">AI</div>
          <div class="workspace-copy"><strong>Insurance lab</strong><span>Personal workspace</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<p class="nav-caption">Workspace</p>', unsafe_allow_html=True)
    for item in NAVIGATION:
        active = st.session_state.page == item["key"]
        wrapper_class = "nav-item-active" if active else ""
        st.markdown(f'<div class="{wrapper_class}">', unsafe_allow_html=True)
        label = item["label"] + ("  ·  Live" if item["key"] == "predict" else "")
        if st.button(label, key=f"nav_{item['key']}", width="stretch"):
            navigate(item["key"])
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<p class="nav-caption">Learn</p>', unsafe_allow_html=True)
    for item in SECONDARY_NAVIGATION:
        active = st.session_state.page == item["key"]
        wrapper_class = "nav-item-active" if active else ""
        st.markdown(f'<div class="{wrapper_class}">', unsafe_allow_html=True)
        if st.button(item["label"], key=f"nav_{item['key']}", width="stretch"):
            navigate(item["key"])
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="sidebar-bottom-block">', unsafe_allow_html=True)
    st.markdown('<div class="support-link">❓ Help &amp; documentation</div>', unsafe_allow_html=True)

    theme_icon = "🌙" if st.session_state.is_dark else "☀️"
    theme_label = "Dark mode" if st.session_state.is_dark else "Light mode"
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(
            f"""<div class="theme-row"><span class="theme-icon">{theme_icon}</span><span>{theme_label}</span></div>""",
            unsafe_allow_html=True,
        )
    with col2:
        if st.button("↺", key="theme_toggle", help="Toggle theme (visual only in this build)"):
            st.session_state.is_dark = not st.session_state.is_dark
            st.rerun()

    st.markdown(
        """
        <div class="profile-row">
          <div class="profile-avatar">AK</div>
          <div class="profile-copy"><strong>Alex Kim</strong><span>Portfolio view</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ---- Top bar ------------------------------------------------------------------
st.markdown(
    f"""
    <div class="topbar">
      <div class="breadcrumbs"><span>Insurance lab</span><span>/</span><strong>{PAGE_TITLES[st.session_state.page]}</strong></div>
      <div class="system-status"><span class="live-pulse"></span> All systems operational</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---- Page router ----------------------------------------------------------
page = st.session_state.page

if page == "predict":
    from pages_predict import render
elif page == "analytics":
    from pages_analytics import render
elif page == "performance":
    from pages_performance import render
elif page == "about":
    from pages_about import render
elif page == "developer":
    from pages_developer import render
else:
    from pages_home import render

render()

# ---- Footer -----------------------------------------------------------------
st.markdown(
    """
    <div style="display:flex; align-items:center; justify-content:space-between; margin-top:40px;
                padding:20px 0; border-top:1px solid var(--line-soft); color:#64738a;
                font-family:'DM Mono', monospace; font-size:10px;">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:grid; place-items:center; width:19px; height:19px; color:var(--mint);
                     background:rgba(142,216,193,.1); border-radius:6px;">✨</span>
        <strong style="color:#aeb9ca; font-family:'Manrope',sans-serif; font-size:11px;">Covera</strong>
        <span>Insurance intelligence, made clear.</span>
      </div>
      <div style="display:flex; align-items:center; gap:16px;">
        <span>Portfolio project · 2024</span>
        <span style="display:flex; align-items:center; gap:6px;"><span class="status-dot status-dot-green"></span> v1.0.0</span>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
