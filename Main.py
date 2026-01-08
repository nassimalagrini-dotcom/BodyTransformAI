import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="BodyTransform AI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium CSS
st.markdown("""
    <style>
    /* Background and Global Settings */
    .stApp { background-color: #000000; color: white; }
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] {display: none;}
    header, footer {visibility: hidden;}

    /* --- TOTAL CENTERING CONTAINER --- */
    .main-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
    }

    .hero-title { 
        font-size: 60px; 
        font-weight: 900; 
        margin-top: 40px;
        color: white; 
    }
    .hero-subtitle { 
        font-size: 18px; 
        opacity: 0.7; 
        color: white; 
        margin-bottom: 50px;
    }

    /* --- THE NEW CENTERED PULSE BUTTON --- */
    .btn-container {
        display: flex;
        justify-content: center;
        width: 100%;
        margin: 40px 0;
    }

    .custom-pulse-button {
        width: 250px;
        height: 250px;
        border: 2px solid white;
        border-radius: 50%;
        background: transparent;
        color: white !important;
        text-decoration: none !important;
        font-size: 16px;
        font-weight: 800;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 1px;
        animation: pulse-ring 2.2s infinite;
        transition: 0.3s ease-in-out;
        cursor: pointer;
    }

    .custom-pulse-button:hover {
        background: white;
        color: black !important;
        box-shadow: 0 0 40px rgba(255, 255, 255, 0.5);
        transform: scale(1.05);
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
        padding: 30px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. CENTERED HERO SECTION
st.markdown("""
    <div class="main-wrapper">
        <h1 class="hero-title">WELCOME TO YOUR JOURNEY</h1>
        <p class="hero-subtitle">Transform Your Life, One Healthy Step at a Time.</p>
    </div>
""", unsafe_allow_html=True)

# 4. THE CENTERED BUTTON (HTML Version for Perfect Alignment)
# Note: On Streamlit Cloud, the path is simply /1_Onboarding
st.markdown("""
    <div class="btn-container">
        <a href="/1_Onboarding" target="_self" class="custom-pulse-button">
            START YOUR<br>TRANSFORMATION
        </a>
    </div>
""", unsafe_allow_html=True)

# 5. BOTTOM CARDS SECTION
st.write("<br><br>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="feature-card"><h1>🍎</h1><p style="color:#b7e4c7; font-weight:800;">PERSONALISED MEAL PLANS</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="feature-card"><h1>❤️</h1><p style="color:#b7e4c7; font-weight:800;">MINDSET & SUPPORT</p></div>', unsafe_allow_html=True)
