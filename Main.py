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
    /* Dark Theme & Hide UI */
    .stApp { background-color: #000000; color: white; }
    [data-testid="stSidebar"], [data-testid="stSidebarNav"], header, footer {display: none !important;}

    /* Centering the Text */
    .hero-text-container {
        text-align: center;
        width: 100%;
        margin-top: 50px;
    }
    .hero-title { font-size: 60px; font-weight: 900; margin-bottom: 5px; }
    .hero-subtitle { font-size: 20px; opacity: 0.8; margin-bottom: 20px; }

    /* --- THE CLICKABLE START BOX --- */
    .start-box {
        border: 2px solid #333;
        border-radius: 20px;
        padding: 60px 20px;
        text-align: center;
        transition: 0.3s;
        cursor: pointer;
        background: rgba(255, 255, 255, 0.03);
    }
    .start-box:hover {
        border-color: white;
        background: rgba(255, 255, 255, 0.1);
        transform: translateY(-5px);
    }
    .start-label {
        font-weight: 800;
        letter-spacing: 2px;
        color: #b7e4c7;
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

# 3. HERO TEXT (Centered)
st.markdown("""
    <div class="hero-text-container">
        <h1 class="hero-title">WELCOME TO YOUR JOURNEY</h1>
        <p class="hero-subtitle">Transform Your Life, One Healthy Step at a Time.</p>
    </div>
""", unsafe_allow_html=True)

# 4. THE START TRIGGER (Using Columns to Force Center)
# We create 3 columns: [Side, Middle, Side]. 
# The middle one (30% width) will contain our clickable element.
col1, col2, col3 = st.columns([1, 1.5, 1])

with col2:
    # We use a container that the user clicks
    st.markdown("""
        <div class="start-box">
            <div style="font-size: 40px; margin-bottom: 10px;">🚀</div>
            <div class="start-label">CLICK HERE TO START</div>
        </div>
    """, unsafe_allow_html=True)
    
    # We place an invisible button over it to handle the logic
    # This prevents the "Page Not Found" error
    if st.button("GO", use_container_width=True, help="Click to start onboarding"):
        st.switch_page("pages/1_Onboarding.py")

# 5. BOTTOM CARDS SECTION
st.write("<br><br>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown('<div class="feature-card"><h1>🍎</h1><p style="color:#b7e4c7; font-weight:800;">PERSONALISED MEAL PLANS</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="feature-card"><h1>❤️</h1><p style="color:#b7e4c7; font-weight:800;">MINDSET & SUPPORT</p></div>', unsafe_allow_html=True)
