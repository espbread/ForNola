import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="I Love You Nolinski 🐯💜",
    page_icon="🐯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Remove default Streamlit margins and match the Agrabah night sky background
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        body, .stApp {
            background-color: #0a031e;
        }
    </style>
""", unsafe_allow_html=True)

html_content = Path(__file__).parent.joinpath("index.html").read_text(encoding="utf-8")
components.html(html_content, height=750, scrolling=False)
