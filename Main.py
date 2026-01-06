import streamlit as st

# 1. Page Config - This also helps hide the sidebar by default
st.set_page_config(
    page_title="BodyTransform AI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Main Premium Dark Theme & Layout Fixes
st.markdown("""
    <style>
    /* Deep Black Background */
    .stApp {
        background-color: #000000;
        color: white;
    }

    /* Force Hide Sidebar on this page specifically */
    [data-testid="stSidebar"] {
        display: none;
    }
    [data-testid="stSidebarNav"] {
        display: none;
    }

    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Hero Section Titles */
    .hero-title {
        text-align: center; 
        font-size: 65px; 
        font-weight: 900; 
        margin-top: 40px;
        margin-bottom: 5px;
        letter-spacing: 2px;
        color: white;
    }
    .hero-subtitle {
        text-align: center; 
        font-size: 20px; 
        opacity: 0.7; 
        margin-bottom: 40px;
        color: white;
    }

    /* --- THE CENTERED PULSE BUTTON FIX --- */
    .stButton {
        display: flex;
        justify-content: center;
        align-items: center;
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
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
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

    /* --- FEATURE CARDS --- */
    .feature-card {
        background-color: #0d0d0d;
        border: 1px solid #222;
        border-radius: 25px;
        padding: 40px;
        text-align: center;
        transition: 0.3s;
    }
    </style>
""", unsafe_allow_html=True)

# 3. HERO SECTION
st.markdown('<h1 class="hero-title">WELCOME TO YOUR JOURNEY</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Transform Your Life, One Healthy Step at a Time.</p>', unsafe_allow_html=True)

# 4. THE CENTERED BUTTON
# We use empty columns to force the button into the center of the grid
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("START YOUR\nTRANSFORMATION"):
        st.switch_page("pages/1_Onboarding.py")

# 5. BOTTOM CARDS SECTION
st.write("<br><br>", unsafe_allow_html=True)
c1, c2 = st.columns(2)

with c1:
    st.markdown("""
        <div class="feature-card">
            <h1 style="font-size: 50px; margin:0;">🍎</h1>
            <p style="color:#b7e4c7; font-weight:800; margin-top:15px; letter-spacing:1.5px;">PERSONALISED<br>MEAL PLANS</p>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="feature-card">
            <h1 style="font-size: 50px; margin:0;">❤️</h1>
            <p style="color:#b7e4c7; font-weight:800; margin-top:15px; letter-spacing:1.5px;">MINDSET &<br>SUPPORT</p>
        </div>
    """, unsafe_allow_html=True)
