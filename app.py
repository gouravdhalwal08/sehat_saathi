import streamlit as st
import database as db
from core.language import TEXT

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sehat Saathi",
    page_icon="🤖",
    layout="wide", # Use "wide" layout for a more modern feel
    initial_sidebar_state="expanded",
)

# --- INITIALIZATION ---
if 'lang' not in st.session_state:
    st.session_state.lang = 'en'

# Function to load and apply CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("assets/style.css")

# --- DATABASE INITIALIZATION ---
db.init_db()

# --- UI TRANSLATION ---
T = TEXT[st.session_state.lang]

# --- SIDEBAR ---
with st.sidebar:
    st.title(T["sidebar_title"])
    selected_lang = st.radio(
        T["lang_select"],
        options=['en', 'hi'],
        format_func=lambda x: "English" if x == 'en' else "हिंदी",
        horizontal=True,
    )
    if selected_lang != st.session_state.lang:
        st.session_state.lang = selected_lang
        st.rerun()

# --- MAIN PAGE CONTENT ---

# Centered title
st.markdown(f"<h1 style='text-align: center;'>{T['home_title']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; font-size: 18px;'>{T['home_intro']}</p>", unsafe_allow_html=True)
st.markdown("---")

st.header(T["home_features_title"])

# --- UPDATED: Apply the "feature-card" CSS class ---
# We use st.markdown with unsafe_allow_html to inject our custom HTML/CSS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="feature-card">
        {T["home_feature_1"]}
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="feature-card">
        {T["home_feature_2"]}
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="feature-card">
        {T["home_feature_3"]}
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True) # Add some spacing
st.warning(T["home_disclaimer"], icon="⚠️")