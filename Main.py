import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="BodyTransform AI",
    page_icon="⚖️",
    layout="wide"
)

# 2. Styles (Native Button Styling)
st.markdown("""
    <style>
    /* Deep Black Background */
    .stApp {
        background-color: #000000;
        color: white;
    }

    /* Hide default header/footer */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Hero Text */
    .hero-title {
        text-align: center; 
        font-size: 65px; 
        font-weight: 900; 
        margin-top: 40px;
        color: white;
    }
    .hero-subtitle {
        text-align: center; 
        font-size: 20px; 
        opacity: 0.7; 
        margin-bottom: 40px;
        color: white;
    }

    /* --- PULSE BUTTON CSS FOR ST.BUTTON --- */
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
        display: block !important;
        margin: 0 auto !important;
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

    /* Feature Cards */
    .feature-card {
        background-color: #0d0d0d;
        border: 1px solid #222;
        border-radius: 25px;
        padding: 40px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. HERO SECTION
st.markdown('<h1 class="hero-title">WELCOME TO YOUR JOURNEY</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Transform Your Life, One Healthy Step at a Time.</p>', unsafe_allow_html=True)

# 4. THE FUNCTIONAL BUTTON
# This native Streamlit button triggers the multipage sidebar
if st.button("START YOUR\nTRANSFORMATION"):
    st.switch_page("pages/1_Onboarding.py")

# 5. BOTTOM CARDS SECTION
st.write("<br><br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="feature-card"><h1 style="font-size: 50px;">🍎</h1><p style="color:#b7e4c7; font-weight:800;">PERSONALISED MEAL PLANS</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="feature-card"><h1 style="font-size: 50px;">❤️</h1><p style="color:#b7e4c7; font-weight:800;">MINDSET & SUPPORT</p></div>', unsafe_allow_html=True)
