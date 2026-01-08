import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="BodyTransform AI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Aggressive Centering CSS
st.markdown("""
    <style>
    /* Dark Theme & Hide UI */
    .stApp { background-color: #000000; color: white; }
    [data-testid="stSidebar"], [data-testid="stSidebarNav"], header, footer {display: none !important;}

    /* --- THE HERO SECTION --- */
    .hero-block {
        text-align: center;
        margin-top: 50px;
        width: 100%;
    }

    .hero-title { 
        font-size: 60px; 
        font-weight: 900; 
        margin-bottom: 5px;
    }

    .hero-subtitle { 
        font-size: 20px; 
        opacity: 0.8; 
        margin-bottom: 40px;
    }

    /* --- THE UNBEATABLE BUTTON CENTERING --- */
    /* This targets the div that Streamlit wraps around every button */
    div.stButton {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
    }

    /* Styling the actual Button component */
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
        line-height: 1.2 !important;
    }

    div.stButton > button:hover {
        background: white !important;
        color: black !important;
        box-shadow: 0 0 50px rgba(255, 255, 255, 0.6) !important;
        transform: scale(1.02) !important;
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
        border-radius: 20px;
        padding: 40px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. HERO TITLES
st.markdown("""
    <div class="hero-block">
        <h1 class="hero-title">WELCOME TO YOUR JOURNEY</h1>
        <p class="hero-subtitle">Transform Your Life, One Healthy Step at a Time.</p>
    </div>
""", unsafe_allow_html=True)

# 4. THE CENTERED BUTTON (Native Streamlit = No "Page Not Found")
# Because we used "div.stButton" flex in the CSS, this WILL be centered.
if st.button("START YOUR\nTRANSFORMATION"):
    st.switch_page("pages/1_Onboarding.py")

# 5. BOTTOM CARDS SECTION
st.write("<br><br>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="feature-card"><h1>🍎</h1><p style="color:#b7e4c7; font-weight:800; text-transform:uppercase;">Personalised Meal Plans</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="feature-card"><h1>❤️</h1><p style="color:#b7e4c7; font-weight:800; text-transform:uppercase;">Mindset & Support</p></div>', unsafe_allow_html=True)
