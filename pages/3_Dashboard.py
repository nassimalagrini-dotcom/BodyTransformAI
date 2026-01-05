import streamlit as st
import pandas as pd
from styles import apply_premium_theme

# 1. Page Setup
st.set_page_config(page_title="Premium Dashboard | BodyTransform AI", page_icon="🚀", layout="wide")
apply_premium_theme()

# --- 2. SECURITY GATEKEEPER ---
if not st.session_state.get('is_pro', False):
    st.warning("🚫 This is a Premium Page. Please unlock it on the Diet Plan page.")
    if st.button("Back to Diet Plan"):
        st.switch_page("pages/2_Diet_Plan.py")
    st.stop()

# --- 3. DYNAMIC DATA & STATE INITIALIZATION ---
user_name = st.session_state.get('user_name', 'Champion')
height = st.session_state.get('height', 170)
age = st.session_state.get('age', 25)
gender = st.session_state.get('gender', 'Male')
activity = st.session_state.get('activity', 'Light Movement')
goal = st.session_state.get('goal', 'Fat Loss')

if 'eaten_meals' not in st.session_state: st.session_state.eaten_meals = []
if 'water_glasses' not in st.session_state: st.session_state.water_glasses = 0
if 'program_day' not in st.session_state: st.session_state.program_day = 1
if 'weight_history' not in st.session_state:
    st.session_state.weight_history = [st.session_state.get('weight', 70.0)]

# --- 4. SMART AI CALORIE RECALCULATION (DAILY) ---
current_weight = st.session_state.weight_history[-1]
# Calculate BMR
bmr = (10 * current_weight) + (6.25 * height) - (5 * age) + (5 if gender == "Male" else -161)
# Apply Activity Multiplier
multipliers = {"Mostly Sitting": 1.2, "Light Movement": 1.375, "Active Job": 1.55, "Very Athletic": 1.725}
tdee = bmr * multipliers.get(activity, 1.375)

# Adjust for Goal
if goal == "Fat Loss":
    target_cal = int(tdee - 500)
elif goal == "Muscle Gain":
    target_cal = int(tdee + 300)
else:
    target_cal = int(tdee)

# Dynamic Meal Values
meal_values = {
    "Breakfast": int(target_cal * 0.25),
    "Lunch": int(target_cal * 0.35),
    "Snack": int(target_cal * 0.15),
    "Dinner": int(target_cal * 0.25)
}
calories_consumed = sum([meal_values[m] for m in st.session_state.eaten_meals])
calories_left = target_cal - calories_consumed

# --- 5. CUSTOM CSS ---
st.markdown("""
    <style>
    .dashboard-card { background: #0d0d0d; border: 1px solid #222; padding: 20px; border-radius: 20px; text-align: center; }
    .metric-value { font-size: 32px; font-weight: 900; color: #ffffff; margin: 0; }
    .metric-label { font-size: 14px; color: #b7e4c7; text-transform: uppercase; font-weight: bold; }
    .streak-badge { background: linear-gradient(135deg, #ff4b2b, #ff416c); color: white; padding: 5px 15px; border-radius: 50px; font-weight: bold; font-size: 12px; }
    .meal-box { background: #151515; padding: 15px; border-radius: 15px; border-left: 5px solid #b7e4c7; margin-bottom: 10px; }
    .meal-eaten { border-left: 5px solid #4CAF50 !important; opacity: 0.5; background: #0a1a0a !important; }
    .unlock-box { background: linear-gradient(90deg, #111 0%, #1a1a1a 100%); border: 2px dashed #b7e4c7; padding: 30px; border-radius: 20px; text-align: center; margin-top: 40px; }
    .recipe-hub-card { background: linear-gradient(135deg, #000000 0%, #1a1a1a 100%); border: 1px solid #b7e4c7; padding: 20px; border-radius: 15px; margin-top: 20px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- 6. WEEKLY REVIEW MILESTONE ---
if st.session_state.program_day % 7 == 0 and not st.session_state.eaten_meals:
    st.balloons()
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); padding: 30px; border-radius: 20px; border: 2px solid #b7e4c7; text-align: center; margin-bottom: 25px;">
            <h2 style="color: #b7e4c7; margin:0;">🌟 WEEK {int(st.session_state.program_day / 7)} COMPLETE! 🌟</h2>
            <p style="color: white;">Consistency is the key to transformation, {user_name}.</p>
        </div>
    """, unsafe_allow_html=True)

# --- 7. HEADER & PROGRESS ---
c1, c2 = st.columns([3, 1])
with c1:
    st.markdown(f"## 👋 Day {st.session_state.program_day}: {user_name}'s Dashboard")
    st.progress(st.session_state.program_day / 30)
with c2:
    st.markdown(f"<div style='text-align:right;'><div class='streak-badge'>🔥 {st.session_state.program_day} DAY STREAK</div></div>", unsafe_allow_html=True)

# --- 8. TODAY'S STATUS ---
st.markdown("### 🟢 Real-Time Targets")
sum_col1, sum_col2, sum_col3 = st.columns(3)
with sum_col1:
    st.markdown(f"<div class='dashboard-card'><p class='metric-label'>Calories Left</p><p class='metric-value'>{max(0, calories_left)}</p><p style='color:#888; font-size:12px;'>kcal (Adjusted)</p></div>", unsafe_allow_html=True)
with sum_col2:
    p_goal = int(current_weight * 2)
    p_now = int((calories_consumed/target_cal)*p_goal) if target_cal > 0 else 0
    st.markdown(f"<div class='dashboard-card'><p class='metric-label'>Protein</p><p class='metric-value'>{p_now}/{p_goal}g</p><p style='color:#888; font-size:12px;'>daily target</p></div>", unsafe_allow_html=True)
with sum_col3:
    st.markdown(f"<div class='dashboard-card'><p class='metric-label'>Water</p><p class='metric-value'>{st.session_state.water_glasses}/8</p><p style='color:#888; font-size:12px;'>glasses logged</p></div>", unsafe_allow_html=True)
    if st.button("🥤 Log Water Glass", use_container_width=True):
        st.session_state.water_glasses += 1
        st.rerun()

# --- 9. WEIGHT JOURNEY ---
st.write("---")
col_chart, col_log = st.columns([2, 1])
with col_chart:
    st.markdown("### 📊 Weight Journey")
    st.line_chart(pd.DataFrame(st.session_state.weight_history, columns=['Weight']), color="#b7e4c7")
    total_change = st.session_state.weight_history[-1] - st.session_state.weight_history[0]
    st.markdown(f"<p style='text-align:center;'>Total Change: <b>{total_change:.1f} kg</b></p>", unsafe_allow_html=True)

with col_log:
    st.markdown("### ⚖️ Daily Weight Log")
    new_w = st.number_input("Log Weight (kg):", value=float(st.session_state.weight_history[-1]), step=0.1)
    if st.button("Update Progress & Recalculate AI", use_container_width=True):
        st.session_state.weight_history.append(new_w)
        st.toast("AI recalibrating your targets...")
        st.rerun()

# --- 10. TODAY'S MENU ---
st.write("### 🍽️ Today's Smart Menu")
m_cols = st.columns(4)
for i, m_name in enumerate(["Breakfast", "Lunch", "Snack", "Dinner"]):
    with m_cols[i]:
        done = m_name in st.session_state.eaten_meals
        box_class = "meal-box meal-eaten" if done else "meal-box"
        st.markdown(f"<div class='{box_class}'><p class='metric-label'>{m_name}</p><p style='font-weight:bold;'>{meal_values[m_name]} kcal</p></div>", unsafe_allow_html=True)
        if not done:
            if st.button(f"Log Meal", key=f"btn_{m_name}", use_container_width=True):
                st.session_state.eaten_meals.append(m_name)
                st.rerun()
        else:
            if st.button("Undo", key=f"undo_{m_name}", use_container_width=True, type="secondary"):
                st.session_state.eaten_meals.remove(m_name)
                st.rerun()

# --- 11. DAY PROGRESSION BUTTON ---
st.markdown(f"""
    <div class='unlock-box'>
        <h3 style='margin:0; color:#b7e4c7;'>Day {st.session_state.program_day} Finished?</h3>
        <p style='color:#888;'>Click to advance. Your calories will re-adjust based on your latest weight.</p>
    </div>
""", unsafe_allow_html=True)

if st.button(f"🏁 UNLOCK DAY {st.session_state.program_day + 1}", use_container_width=True, type="primary"):
    st.session_state.program_day += 1
    st.session_state.eaten_meals = []
    st.session_state.water_glasses = 0
    st.balloons()
    st.rerun()

# --- 12. ELITE HUB LINK (NEW) ---
st.markdown("""
    <div class='recipe-hub-card'>
        <h3 style='color:#b7e4c7; margin-bottom:5px;'>💎 Elite Recipe Hub</h3>
        <p style='color:#fff; font-size:14px;'>Access international recipes, instructions, and your Weekly PDF Plan.</p>
    </div>
""", unsafe_allow_html=True)

if st.button("📖 Open Elite Recipes & PDF Hub", use_container_width=True):
    st.switch_page("pages/4_Pro_Hub.py") # Ensure your success page is named 4_Pro_Hub.py

# --- 13. NAVIGATION & SUPPORT ---
st.write("---")
nav1, nav2, nav3 = st.columns(3)
if nav1.button("🥗 View My Diet Plan", use_container_width=True): st.switch_page("pages/2_Diet_Plan.py")

with nav2:
    with st.popover("🆘 Support", use_container_width=True):
        st.write("Need help with your plan?")
        st.markdown(f"Contact: `lagrininassima@gmail.com`")
        st.markdown(f"Client ID: `{st.session_state.get('client_id', 'N/A')}`")

if nav3.button("🔄 Reset Today", use_container_width=True):
    st.session_state.eaten_meals = []
    st.session_state.water_glasses = 0
    st.rerun()
