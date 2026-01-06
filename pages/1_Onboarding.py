import streamlit as st
import uuid
import os
import pandas as pd
from datetime import datetime

# 1. Page Config - This brings the sidebar back once they enter the onboarding
st.set_page_config(
    page_title="Join BodyTransform AI", 
    page_icon="💪",
    initial_sidebar_state="expanded"
)

# --- NAVIGATION & THEME ---
# Custom CSS to make sure the sidebar is visible on this page
st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: flex !important; }
    [data-testid="stSidebarNav"] { display: flex !important; }
    </style>
""", unsafe_allow_html=True)

# "Back to Home" Button at the very top
if st.button("⬅️ Back to Home"):
    st.switch_page("Main.py")

st.write("---")

st.title("🚀 Start Your Transformation")

# Initialize session state for name if not present
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ""

# --- STEP 1: NAME INPUT ---
if not st.session_state['user_name']:
    st.subheader("First, let's get to know you.")
    name_input = st.text_input("What is your name?", placeholder="Enter your name...")

    if st.button("Continue ➡️"):
        if name_input:
            st.session_state['user_name'] = name_input
            # Generate Unique ID immediately
            unique_hex = str(uuid.uuid4()).upper()[:6]
            st.session_state['client_id'] = f"BT-{unique_hex}"
            st.rerun()
        else:
            st.warning("Please enter your name.")

# --- STEP 2: FULL DETAILS ---
else:
    st.success(f"Welcome, {st.session_state['user_name']}! (ID: {st.session_state['client_id']})")

    # Unit Selection Toggle
    unit_system = st.radio("Preferred Units:", ["Metric (kg/cm)", "Imperial (lbs/ft)"], horizontal=True)

    with st.form("onboarding_form"):
        col1, col2 = st.columns(2)

        with col1:
            gender = st.selectbox("Gender", ["Female", "Male", "Other"])
            age = st.number_input("Age", min_value=15, max_value=90, value=25)

            # Weight Conversion Logic
            if unit_system == "Metric (kg/cm)":
                input_weight = st.number_input("Weight (kg)", min_value=30.0, max_value=300.0, value=70.0)
                final_weight = input_weight
            else:
                weight_lbs = st.number_input("Weight (lbs)", min_value=70.0, max_value=600.0, value=155.0)
                final_weight = weight_lbs * 0.453592  # Converts to kg

        with col2:
            # Height Conversion Logic
            if unit_system == "Metric (kg/cm)":
                input_height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)
                final_height = input_height
            else:
                f_col, i_col = st.columns(2)
                feet = f_col.number_input("Feet", min_value=3, max_value=8, value=5)
                inches = i_col.number_input("Inches", min_value=0, max_value=11, value=7)
                final_height = (feet * 30.48) + (inches * 2.54)  # Converts to cm

            activity = st.selectbox("Activity Level",
                                    ["Mostly Sitting", "Light Movement", "Active Job", "Very Athletic"])
            goal = st.selectbox("Main Goal", ["Fat Loss", "Muscle Gain", "Maintenance"])

        st.write("---")
        diet_choice = st.selectbox("Dietary Preference", ["Normal", "Vegan", "Halal", "Intermittent Fasting"])

        if st.form_submit_button("GENERATE MY PLAN 🥗"):
            # Update session state
            st.session_state.update({
                "weight": final_weight,
                "height": final_height,
                "age": age,
                "gender": gender,
                "activity": activity,
                "goal": goal,
                "diet": diet_choice,
                "unit_pref": unit_system,
                "onboarding_complete": True
            })
            
            # Switch to Diet Plan
            st.switch_page("pages/2_Diet_Plan.py")

    # Reset button to go back to Name Step
    if st.button("Edit Name"):
        st.session_state['user_name'] = ""
        st.rerun()
