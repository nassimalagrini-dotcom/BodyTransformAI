import streamlit as st
import pandas as pd
from styles import apply_premium_theme

# 1. Page Setup & Styling
st.set_page_config(page_title="My Diet Plan | BodyTransform AI", page_icon="🥗", layout="wide")
apply_premium_theme()

st.markdown("""
    <style>
    [data-testid="stMetric"] {
        background-color: #111111 !important;
        border: 1px solid #222222 !important;
        padding: 20px !important;
        border-radius: 15px !important;
        text-align: center !important;
    }
    .meal-card {
        background-color: #0d0d0d;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #b7e4c7;
        margin-bottom: 20px;
    }
    .sale-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); 
        padding: 30px; border-radius: 25px; border: 1px solid #00d4ff; text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Safety Check
if 'weight' not in st.session_state:
    st.error("Please complete the onboarding first!")
    st.stop()

# 3. Data Retrieval
user_name = st.session_state.get('user_name', 'Champion')
client_id = st.session_state.get('client_id', 'BT-XXXXXX')
weight = st.session_state['weight']
height = st.session_state['height']
age = st.session_state['age']
gender = st.session_state['gender']
activity = st.session_state.get('activity', 'Light Movement')
diet_type = st.session_state.get('diet', 'Normal')
goal = st.session_state.get('goal', 'Fat Loss')
day_count = st.session_state.get('program_day', 1)

# 4. Calculation Engine
bmr = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "Male" else -161)
multipliers = {"Mostly Sitting": 1.2, "Light Movement": 1.375, "Active Job": 1.55, "Very Athletic": 1.725}
tdee = bmr * multipliers.get(activity, 1.375)

if goal == "Fat Loss":
    target_calories = int(tdee - 500)
elif goal == "Muscle Gain":
    target_calories = int(tdee + 300)
else:
    target_calories = int(tdee)

st.session_state['target_calories'] = target_calories


# 5. Dynamic Meal Logic with Exact Ingredient Weights
def get_dynamic_meal(meal_key, meal_calories):
    if meal_calories <= 0: return ""
    prot_cal = int(meal_calories * 0.4)
    other_cal = int(meal_calories - prot_cal)
    variety_index = day_count % 3

    # Define calorie densities (kcal per gram)
    densities = {
        "Chicken Breast": 1.65, "Salmon Fillet": 2.0, "Lean Beef": 2.5,
        "Halal Chicken": 1.65, "Halal Beef": 2.5, "Halal Lamb": 2.9,
        "Tofu": 1.0, "Tempeh": 1.9, "Seitan": 3.7,
        "Brown Rice": 1.1, "Sweet Potato": 0.86, "Quinoa": 1.2,
        "Granola": 4.0, "Berries": 0.3, "Oats": 3.8, "Bread": 2.5,
        "Greek Yogurt": 0.6, "Nuts": 6.0, "Peanut Butter": 5.9
    }

    if diet_type == "Vegan":
        proteins = ["Tofu", "Tempeh", "Seitan"]
        p_name = proteins[variety_index]
    elif diet_type == "Halal":
        proteins = ["Halal Chicken", "Halal Beef", "Halal Lamb"]
        p_name = proteins[variety_index]
    else:
        proteins = ["Chicken Breast", "Salmon Fillet", "Lean Beef"]
        p_name = proteins[variety_index]

    carbs = [
        {"name": "Brown Rice", "veg": "Broccoli"},
        {"name": "Sweet Potato", "veg": "Asparagus"},
        {"name": "Quinoa", "veg": "Spinach"}
    ]
    daily_carb = carbs[variety_index]

    # Render Breakfast with specific weights
    if meal_key == "b":
        if diet_type == "Vegan":
            return f"🥣 **Chia Seed Pudding ({int(prot_cal / 4.9)}g)**: {prot_cal} kcal  \n🥑 **Avocado ({int(other_cal / 1.6)}g) on Toast**: {other_cal} kcal"

        if day_count % 2 == 0:
            num_eggs = max(2, int(prot_cal / 70))
            bread_g = int(other_cal / densities["Bread"])
            return f"🍳 **{num_eggs} Eggs**: {num_eggs * 70} kcal  \n🍞 **Whole Grain Bread ({bread_g}g)**: {other_cal} kcal"
        else:
            berry_cal = int(other_cal * 0.2)
            granola_cal = int(other_cal * 0.8)
            return f"🍶 **Greek Yogurt ({int(prot_cal / densities['Greek Yogurt'])}g)**: {prot_cal} kcal \n🍓 **Berries ({int(berry_cal / densities['Berries'])}g)** & **Granola ({int(granola_cal / densities['Granola'])}g)**: {other_cal} kcal"

    # Render Snack with specific weights
    if meal_key == "s":
        snacks = [
            f"🥜 **Mixed Nuts ({int(meal_calories / densities['Nuts'])}g)**",
            f"🍏 **Apple (150g)** & **Peanut Butter ({int((meal_calories - 75) / densities['Peanut Butter'])}g)**",
            f"🍶 **Protein Shake (1 Scoop)** & **Almonds ({int((meal_calories - 120) / densities['Nuts'])}g)**"
        ]
        return f"{snacks[variety_index]}: {meal_calories} kcal"

    # Cheat Day Logic
    if day_count % 7 == 0:
        return f"🍕 **WEEKLY REWARD MEAL**: Enjoy a balanced favorite meal! Keep it within {meal_calories} kcal."

    # Render Lunch/Dinner with specific weights
    p_grams = int(prot_cal / densities[p_name])
    c_grams = int(other_cal / densities[daily_carb['name']])
    return f"🍱 **{p_name} ({p_grams}g)**: {prot_cal} kcal  \n🥗 **{daily_carb['name']} ({c_grams}g)** & **{daily_carb['veg']}**: {other_cal} kcal"


# --- UI DISPLAY ---
st.title(f"🍽️ Day {day_count}: {user_name}'s {diet_type} Plan")
st.write(f"🆔 **Unique Client ID:** `{client_id}`")

ramadan_mode = st.toggle("Enable Ramadan Mode 🌙", value=False)
st.write("---")

# 7. Meal Rendering
if ramadan_mode:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='meal-card'> 🌅 Suhoor</div>", unsafe_allow_html=True)
        st.write(get_dynamic_meal("b", int(target_calories * 0.45)))
    with c2:
        st.markdown("<div class='meal-card'>🌙 Iftar</div>", unsafe_allow_html=True)
        st.write(f"🏮 **3 Dates & Water**: 60 kcal")
        st.write(get_dynamic_meal("l", int(target_calories * 0.55) - 60))
elif diet_type == "Intermittent Fasting":
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='meal-card'> 🥗 Meal 1 (1:00 PM)</div>", unsafe_allow_html=True)
        st.write(get_dynamic_meal("l", int(target_calories * 0.55)))
    with c2:
        st.markdown("<div class='meal-card'>🍽️ Meal 2 (8:00 PM)</div>", unsafe_allow_html=True)
        st.write(get_dynamic_meal("d", int(target_calories * 0.45)))
else:
    m_cols = st.columns(4)
    ratios = {"Breakfast": 0.25, "Lunch": 0.35, "Snack": 0.15, "Dinner": 0.25}
    keys = {"Breakfast": "b", "Lunch": "l", "Snack": "s", "Dinner": "d"}
    for i, (name, ratio) in enumerate(ratios.items()):
        with m_cols[i]:
            st.markdown(f"<div class='meal-card'><h4>{name}</h4><b>{int(target_calories * ratio)} kcal</b></div>",
                        unsafe_allow_html=True)
            st.write(get_dynamic_meal(keys[name], int(target_calories * ratio)))

# 8. DAILY TARGETS
st.write("---")
st.markdown("### 📊 Daily Targets")
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1: st.metric("Calories", f"{target_calories} kcal")
with col_m2: st.metric("Protein", f"{int(weight * 2)}g")
with col_m3: st.metric("Water", "3.0 L")

# --- 8.5 WEEKLY SHOPPING LIST ---
st.write("---")
with st.expander("🛒 Generate My Weekly Shopping List"):
    st.markdown("### Your Weekly Grocery Essentials")
    if diet_type == "Vegan":
        proteins = "Tofu, Tempeh, Seitan, Lentils"
    elif diet_type == "Halal":
        proteins = "Halal Chicken, Halal Beef, Halal Lamb"
    else:
        proteins = "Chicken Breast, Salmon Fillets, Lean Beef, Eggs"

    col_l1, col_l2 = st.columns(2)
    with col_l1:
        st.markdown("**🥩 Proteins**")
        st.write(f"- {proteins}")
        st.markdown("**🥦 Produce**")
        st.write("- Broccoli, Spinach, Asparagus, Berries")
    with col_l2:
        st.markdown("**🍚 Carbohydrates**")
        st.write("- Brown Rice, Sweet Potato, Quinoa, Oats")
        st.markdown("**🥑 Healthy Fats**")
        st.write("- Olive Oil, Avocado, Mixed Nuts")

# --- 9. PREMIUM UPSELL & PAYPAL ---
st.write("<br>", unsafe_allow_html=True)
st.markdown(f"""
    <div class="sale-box">
        <h2 style="color: #ffffff; margin-bottom: 5px;">🔥 UNLOCK PREMIUM DASHBOARD</h2>
        <p style="color: #00d4ff; font-weight: bold;">ONLY $3.99 • ONE-TIME PAYMENT</p>
        <p style="color: white; font-size: 14px;">Unlock advanced weight tracking and your full 30-day journey.</p>
    </div>
""", unsafe_allow_html=True)

paypal_url = f"https://www.paypal.me/BodytransformationIA/3.99?item_name=Premium_Activation_{client_id}"

col_pay_1, col_pay_2, col_pay_3 = st.columns([1, 2, 1])
with col_pay_2:
    if st.button("💳 PAY WITH PAYPAL", use_container_width=True, type="primary"):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={paypal_url}">', unsafe_allow_html=True)

# --- 10. ACCESS CODE CHECKER & SUPPORT ---
st.write("---")
col_lock, col_supp = st.columns([2, 1])
with col_lock:
    with st.expander("🔓 Already Paid? Enter Your Activation Key", expanded=True):
        st.write(f"Your ID: **{client_id}**")
        user_key = st.text_input("Activation Key", type="password")
        correct_key = f"{client_id.replace('-', '')}-2026"
        if st.button("Activate Dashboard 🚀", use_container_width=True):
            if user_key == correct_key:
                st.session_state['is_pro'] = True
                st.switch_page("pages/3_Dashboard.py")
            else:
                st.error("Invalid Key.")

with col_supp:
    with st.expander("🆘 Support"):
        mailto = f"mailto:nassima.lagrini@gmail.com?subject=Support:{client_id}"
        st.markdown(
            f'<a href="{mailto}" style="text-decoration:none;"><div style="background:#222; color:white; padding:10px; border-radius:5px; text-align:center;">📧 Email Support</div></a>',
            unsafe_allow_html=True)

if st.button("⬅️ Return to Dashboard"):
    st.switch_page("pages/3_Dashboard.py")