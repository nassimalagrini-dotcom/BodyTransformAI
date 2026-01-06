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
    .stApp { background-color: #000000; color: white; }
    
    /* Hide Sidebar and Header */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] {display: none;}
    header, footer {visibility: hidden;}

    .hero-title {
        text-align: center; font-size: 65px; font-weight: 900; 
        margin-top: 40px; margin-bottom: 5px; color: white;
    }
    .hero-subtitle {
        text-align: center; font-size: 20px; opacity: 0.7; margin-bottom: 40px; color: white;
    }

    /* --- THE PULSE CIRCLE --- */
    .button-container {
        display: flex; justify-content: center; align-items: center;
        width: 100%; margin: 50px 0; position: relative;
    }

    .pulse-circle {
        width: 260px; height: 260px; border: 2px solid white; border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        text-align: center; color: white; font-size: 18px; font-weight: 800;
        text-transform: uppercase; animation: pulse-ring 2.2s infinite;
        font-family: 'Inter', sans-serif; pointer-events: none;
    }

    @keyframes pulse-ring {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.4); }
        70% { transform: scale(1.05); box-shadow: 0 0 0 30px rgba(255, 255, 255, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0); }
    }

    /* --- THE INVISIBLE CLICKER --- */
    .stButton {
        position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        display: flex; justify-content: center; align-items: center;
    }
    
    /* Making the actual streamlit button invisible but clickable */
    div.stButton > button {
        width: 260px !important; height: 260px !important;
        background: transparent !important; color: transparent !important;
        border: none !important; border-radius: 50% !important;
        cursor: pointer !important; z-index: 10;
    }
    div.stButton > button:hover {
        background: rgba(255,255,255,0.1) !important;
    }

    .feature-card {
        background-color: #0d0d0d; border: 1px solid #222;
        border-radius: 25px; padding: 40px; text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. HERO SECTION
st.markdown('<h1 class="hero-title">WELCOME TO YOUR JOURNEY</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Transform Your Life, One Healthy Step at a Time.</p>', unsafe_allow_html=True)

# 4. THE CENTERED BUTTON (Design + Function combined)
st.markdown('<div class="button-container"><div class="pulse-circle">START YOUR<br>TRANSFORMATION</div>', unsafe_allow_html=True)
if st.button(" "): # This space makes the button invisible
    st.switch_page("pages/1_Onboarding.py")
st.markdown('</div>', unsafe_allow_html=True)

# 5. BOTTOM CARDS
st.write("<br><br>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="feature-card"><h1 style="font-size: 50px;">🍎</h1><p style="color:#b7e4c7; font-weight:800;">PERSONALISED MEAL PLANS</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="feature-card"><h1 style="font-size: 50px;">❤️</h1><p style="color:#b7e4c7; font-weight:800;">MINDSET & SUPPORT</p></div>', unsafe_allow_html=True)
