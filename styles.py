import streamlit as st

def apply_premium_theme():
    st.markdown("""
    <style>
    body {
        background-color: #FAFAF8;
        color: #1F2933;
    }
    .stButton>button {
        background-color: #2FBF9E;
        color: white;
        border-radius: 16px;
        height: 48px;
        font-size: 16px;
        border: none;
    }
    .stMetric {
        background: white;
        padding: 16px;
        border-radius: 16px;
    }
    </style>
    """, unsafe_allow_html=True)
