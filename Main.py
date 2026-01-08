import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="BodyTransform AI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Complete CSS Overhaul
st.markdown("""
    <style>
    /* Dark Theme & Hide UI */
    .stApp { background-color: #000000; color: white; }
    [data-testid="stSidebar"], [data-testid="stSidebarNav"], header, footer {display: none !important;}

    /* THE MASTER CONTAINER (Forces everything to center) */
    .center-everything {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        padding-top: 50px;
    }

    .hero-title { 
        font-size: 60px; 
        font-weight: 900; 
        margin-bottom: 10px;
    }

    .hero-subtitle { 
        font-size: 20px; 
        opacity: 0.8; 
        margin-bottom: 40px;
    }

    /* THE PULSE BUTTON STYLE */
    .pulse-btn {
        width: 280px;
        height: 280px;
        border: 2px solid white;
        border-radius: 50%;
        background: transparent;
        color: white !important;
        text-decoration: none !important;
        font-size: 18px;
        font-weight: 800;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        text-transform: uppercase;
        animation: pulse-ring 2.2s infinite;
        transition: 0.3s;
        cursor: pointer;
        border-style: solid;
    }

    .pulse-btn:hover {
        background: white;
        color: black !important;
        box-shadow: 0 0 50px rgba(255, 255, 255, 0.6);
    }

    @keyframes pulse-ring {
        0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.4); }
        70% { transform: scale(1.05); box-shadow: 0 0 0 30px rgba(255, 255, 255, 0); }
        100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0); }
    }

    /* Feature Cards */
    .card-container { margin-top: 60px; }
    .feature-card {
        background-color: #0d0d0d;
        border: 1px solid #222;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. THE CENTERED HERO & BUTTON (All in one HTML block)
# This prevents Streamlit from moving the button to the left.
st.markdown("""
    <div class="center-everything">
        <h1 class="hero-title">WELCOME TO YOUR JOURNEY</h1>
        <p class="hero-subtitle">Transform Your Life, One Healthy Step at a Time.</p>
        <a href="/1_Onboarding" target="_self" class="pulse-btn">
            START YOUR<br>TRANSFORMATION
        </a>
    </div>
""", unsafe_allow_html=True)

# 4. BOTTOM CARDS SECTION
st.markdown('<div class="card-container">', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="feature-card"><h1>🍎</h1><p style="color:#b7e4c7; font-weight:800;">PERSONALISED MEAL PLANS</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="feature-card"><h1>❤️</h1><p style="color:#b7e4c7; font-weight:800;">MINDSET & SUPPORT</p></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
