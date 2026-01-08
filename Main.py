import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="BodyTransform AI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium CSS for the Clickable Hero
st.markdown("""
    <style>
    /* Dark Theme & Hide UI */
    .stApp { background-color: #000000; color: white; }
    [data-testid="stSidebar"], [data-testid="stSidebarNav"], header, footer {display: none !important;}

    /* --- THE CLICKABLE HERO CARD --- */
    .hero-card {
        background: linear-gradient(145deg, #0a0a0a, #1a1a1a);
        border: 1px solid #333;
        border-radius: 30px;
        padding: 80px 40px;
        margin: 40px auto;
        max-width: 800px;
        text-align: center;
        transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
        display: block;
        text-decoration: none !important;
        color: white !important;
    }

    .hero-card:hover {
        border-color: #ffffff;
        transform: scale(1.02);
        box-shadow: 0 0 50px rgba(255, 255, 255, 0.1);
        background: linear-gradient(145deg, #111, #222);
    }

    .hero-title { 
        font-size: 55px; 
        font-weight: 900; 
        margin-bottom: 15px;
        letter-spacing: -1px;
    }

    .hero-subtitle { 
        font-size: 20px; 
        opacity: 0.7; 
        margin-bottom: 40px;
    }

    .action-text {
        font-size: 14px;
        font-weight: 800;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #b7e4c7;
        border: 1px solid #b7e4c7;
        padding: 12px 30px;
        border-radius: 50px;
        display: inline-block;
    }

    /* Feature Cards Section */
    .feature-card {
        background-color: #0d0d0d;
        border: 1px solid #222;
        border-radius: 25px;
        padding: 40px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. THE NEW WAY TO START (Clickable Hero Section)
# This uses a standard anchor tag that wraps the whole hero section
st.markdown("""
    <a href="/1_Onboarding" target="_self" style="text-decoration: none;">
        <div class="hero-card">
            <h1 class="hero-title">WELCOME TO YOUR JOURNEY</h1>
            <p class="hero-subtitle">Transform Your Life, One Healthy Step at a Time.</p>
            <div class="action-text">Click Anywhere to Start →</div>
        </div>
    </a>
""", unsafe_allow_html=True)

# 4. BOTTOM CARDS SECTION
st.write("<br>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="feature-card"><h1>🍎</h1><p style="color:#b7e4c7; font-weight:800; text-transform:uppercase;">Personalised Meal Plans</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="feature-card"><h1>❤️</h1><p style="color:#b7e4c7; font-weight:800; text-transform:uppercase;">Mindset & Support</p></div>', unsafe_allow_html=True)
