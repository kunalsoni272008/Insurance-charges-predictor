import streamlit as st

from components import page_title, section_label, surface_open, surface_close, tag
from data import DEVELOPER_SKILLS

SKILL_ACCENTS = ["var(--blue)", "var(--mint)", "var(--peach)", "var(--lilac)"]


def render():
    st.markdown('<div class="page-enter">', unsafe_allow_html=True)

    page_title(
        "Developer",
        "The person behind the model.",
        "A little context on the builder, the thinking, and the craft behind Covera.",
        action_html=tag("Open to opportunities", "blue"),
    )

    surface_open("")
    p_col, intro_col, aside_col = st.columns([0.28, 1.0, 0.32], gap="medium")
    with p_col:
        st.markdown(
            """
            <div class="developer-portrait">
              <span class="portrait-initials">AK</span>
              <span class="portrait-status"><span class="status-dot status-dot-green"></span> Available</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with intro_col:
        section_label("Hi, I'm Alex")
        st.markdown(
            '<h2 style="margin:0; color:var(--white); font-size:clamp(20px,2.6vw,28px); letter-spacing:-.03em; line-height:1.2;">'
            "I build thoughtful products at the intersection of data and people.</h2>",
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="color:var(--muted); font-size:12px; line-height:1.7; margin:12px 0 16px;">'
            "I'm a machine learning practitioner focused on making complex systems feel clear, useful, and human. "
            "Covera is a portfolio study in doing exactly that.</p>",
            unsafe_allow_html=True,
        )
        b1, b2 = st.columns([1, 1.4])
        with b1:
            st.button("Let's connect →", key="dev_connect")
        with b2:
            st.markdown(
                '<a href="mailto:hello@alexkim.dev" style="display:inline-flex; align-items:center; gap:8px; '
                'height:42px; padding:0 16px; color:var(--white); background:rgba(255,255,255,.07); '
                'border:1px solid rgba(255,255,255,.13); border-radius:10px; font-size:11px; font-weight:700;">'
                "Send an email ✉️</a>",
                unsafe_allow_html=True,
            )
    with aside_col:
        st.markdown(
            """
            <div style="display:flex; flex-direction:column; gap:16px; padding-left:16px; border-left:1px solid var(--line-soft);">
              <div><span style="color:#6d7b92; font-family:'DM Mono',monospace; font-size:9px;">Based in</span><br/>
                   <strong style="color:#bbc7d8; font-size:10.5px;">New Delhi, India</strong></div>
              <div><span style="color:#6d7b92; font-family:'DM Mono',monospace; font-size:9px;">Focus</span><br/>
                   <strong style="color:#bbc7d8; font-size:10.5px;">Applied ML + product</strong></div>
              <div><span style="color:#6d7b92; font-family:'DM Mono',monospace; font-size:9px;">Currently</span><br/>
                   <strong style="color:#bbc7d8; font-size:10.5px; display:flex; align-items:center; gap:6px;">
                     <span class="status-dot status-dot-green"></span>Building</strong></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    surface_close()

    st.write("")

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        surface_open("")
        st.markdown(
            '<div style="display:flex; align-items:flex-start; justify-content:space-between;">'
            '<div><p class="section-label">Toolkit</p>'
            '<h3 style="margin:0; color:var(--white); font-size:17px; letter-spacing:-.02em;">Skills I use to ship.</h3></div>'
            '<span style="color:var(--blue);">💻</span></div>',
            unsafe_allow_html=True,
        )
        rows_html = ""
        for i, skill in enumerate(DEVELOPER_SKILLS):
            rows_html += f"""
            <div class="skill-row"><span>{str(i + 1).zfill(2)}</span><strong style="color:{SKILL_ACCENTS[i % 4]};">{skill}</strong></div>
            """
        st.markdown(f'<div style="margin-top:18px;">{rows_html}</div>', unsafe_allow_html=True)
        surface_close()

    with col2:
        surface_open("")
        st.markdown('<div style="font-size:19px;">✨</div>', unsafe_allow_html=True)
        section_label("Working philosophy")
        st.markdown(
            '<h3 style="margin:0; color:var(--white); font-size:19px; letter-spacing:-.02em;">Good AI should explain itself.</h3>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="color:#8794aa; font-size:11px; line-height:1.75; margin:12px 0 24px;">'
            "The best model is not always the most complex one. It is the one that creates enough confidence for "
            "a person to make their next decision.</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div style="width:70px; height:2px; background:linear-gradient(90deg, var(--mint), transparent);"></div>'
            '<span style="display:block; margin-top:10px; color:#71849a; font-family:\'DM Mono\',monospace; font-size:9px;">'
            "Curiosity over complexity</span>",
            unsafe_allow_html=True,
        )
        surface_close()

    st.write("")
    section_label("Elsewhere")
    st.markdown(
        '<h2 style="margin:0 0 20px; color:var(--white); font-size:24px; letter-spacing:-.03em;">'
        'Let\'s build something <em class="hl">considered.</em></h2>',
        unsafe_allow_html=True,
    )

    links = [
        ("GH", "var(--blue)", "GitHub", "Projects & experiments", "https://github.com"),
        ("in", "var(--blue)", "LinkedIn", "Professional profile", "https://linkedin.com"),
        ("@", "var(--peach)", "Email", "hello@alexkim.dev", "mailto:hello@alexkim.dev"),
        ("⬇", "var(--mint)", "Resume", "Download profile", "#"),
    ]
    lcols = st.columns(2)
    for i, (letter, color, title, sub, href) in enumerate(links):
        with lcols[i % 2]:
            st.markdown(
                f"""
                <a href="{href}" target="_blank" class="external-link" style="text-decoration:none;">
                  <span class="link-letter" style="color:{color}; background:rgba(255,255,255,.06);">{letter}</span>
                  <span><strong>{title}</strong><small>{sub}</small></span>
                </a>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    fc1, fc2 = st.columns([2, 1])
    with fc1:
        st.markdown(
            '<div style="display:flex; align-items:center; height:42px; color:#6b7a90; font-family:\'DM Mono\',monospace; font-size:10px;">'
            'Thanks for taking a closer look.</div>',
            unsafe_allow_html=True,
        )
    with fc2:
        st.button("View project source →", key="dev_source")

    st.markdown("</div>", unsafe_allow_html=True)
