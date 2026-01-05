import streamlit as st

# 1. Page Config
st.set_page_config(
    page_title="BodyTransform AI",
    page_icon="⚖️",
    layout="wide"
)

# 2. Main Premium Dark Theme
st.markdown("""
    <style>
    /* Deep Black Background */
    .stApp {
        background-color: #000000;
        color: white;
    }

    /* Hide default Streamlit elements for a cleaner look */
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

    /* --- THE CENTERED PULSE BUTTON --- */
    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin: 50px 0;
    }

    .pulse-button {
        width: 260px;
        height: 260px;
        border: 2px solid white;
        border-radius: 50%;
        background: transparent;
        color: white !important;      /* Forces text to white */
        text-decoration: none !important; /* Removes blue underline */
        font-size: 18px;
        font-weight: 800;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        cursor: pointer;
        text-transform: uppercase;
        animation: pulse-ring 2.2s infinite;
        transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        font-family: 'Inter', sans-serif;
    }

    .pulse-button:hover {
        background: white;
        color: black !important;
        box-shadow: 0 0 50px rgba(255, 255, 255, 0.6);
        text-decoration: none !important;
        transform: scale(1.05);
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
        min-height: 250px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        transition: 0.3s;
    }

    .feature-card:hover {
        border-color: #444;
        background-color: #151515;
    }

    .feature-text {
        color: #b7e4c7 !important;
        font-weight: 800;
        margin-top: 15px;
        font-size: 14px;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# 3. HERO SECTION
st.markdown('<h1 class="hero-title">WELCOME TO YOUR JOURNEY</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Transform Your Life, One Healthy Step at a Time.</p>', unsafe_allow_html=True)

# 4. THE CENTERED BUTTON
# Using HTML for the link to ensure it stays centered and follows our styling
st.markdown("""
    <div class="button-container">
        <a href="/Onboarding" target="_self" class="pulse-button">
            START YOUR<br>TRANSFORMATION
        </a>
    </div>
""", unsafe_allow_html=True)

# 5. BOTTOM CARDS SECTION
st.write("<br><br>", unsafe_allow_html=True)
c1, c3 = st.columns(2)

with c1:
    st.markdown("""
        <div class="feature-card">
            <h1 style="font-size: 50px; margin:0;">🍎</h1>
            <p class="feature-text">PERSONALISED<br>MEAL PLANS</p>
        </div>
    """, unsafe_allow_html=True)


with c3:
    st.markdown("""
        <div class="feature-card">
            <h1 style="font-size: 50px; margin:0;">❤️</h1>
            <p class="feature-text">MINDSET &<br>SUPPORT</p>
        </div>
    """, unsafe_allow_html=True)

# Social Proof Footer
st.markdown("""
    <p style='text-align: center; margin-top: 60px; opacity: 0.4; font-size: 14px;'>
        Join thousands of success stories!
    </p>
""", unsafe_allow_html=True)