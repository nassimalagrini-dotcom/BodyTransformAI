import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="BodyTransform AI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Main Premium Dark Theme
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: white;
    }

    /* Force Hide Sidebar */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] {display: none;}
    header, footer {visibility: hidden;}

    /* HERO TITLES */
    .hero-container {
        text-align: center;
        margin-top: 5vh;
    }
    .hero-title { font-size: 65px; font-weight: 900; color: white; margin-bottom: 0px; }
    .hero-subtitle { font-size: 20px; opacity: 0.7; color: white; }

    /* --- THE ULTIMATE CENTERING FIX --- */
    .stButton {
        display: flex;
        justify-content: center;
        margin-top: 50px;
    }

    div.stButton > button {
        width: 280px !important;
        height: 280px !important;
        border: 2px solid white !important;
        border-radius: 50% !important;
        background: transparent !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        animation: pulse-ring 2.2s infinite !important;
        transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    div.stButton > button:hover {
        background: white !important;
        color: black !important;
        box-shadow: 0 0 50px rgba(255, 255, 255, 0.6) !important;
        transform: scale(1.05) !important;
    }

    @keyframes pulse-ring {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.4); }
        70% { transform: scale(1.05); box-shadow: 0 0 0 30px rgba(255, 255, 255, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0); }
    }

    /* FEATURE CARDS */
    .feature-container { margin-top: 100px; }
    .feature-card {
        background-color: #0d0d0d;
        border: 1px solid #222;
        border-radius: 25px;
        padding: 30px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. CONTENT
st.markdown('<div class="hero-container"><h1 class="hero-title">WELCOME TO YOUR JOURNEY</h1><p class="hero-subtitle">Transform Your Life, One Healthy Step at a Time.</p></div>', unsafe_allow_html=True)

# 4. THE CENTERED BUTTON
if st.button("START YOUR\nTRANSFORMATION"):
    st.switch_page("pages/1_Onboarding.py")

# 5. BOTTOM CARDS
st.markdown('<div class="feature-container">', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="feature-card"><h1 style="font-size: 40px;">🍎</h1><p style="color:#b7e4c7; font-weight:800;">PERSONALISED MEAL PLANS</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="feature-card"><h1 style="font-size: 40px;">❤️</h1><p style="color:#b7e4c7; font-weight:800;">MINDSET & SUPPORT</p></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
