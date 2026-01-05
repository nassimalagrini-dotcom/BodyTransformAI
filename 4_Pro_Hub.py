import streamlit as st
from styles import apply_premium_theme
from fpdf import FPDF

# 1. Page Setup
st.set_page_config(page_title="Elite Pro Hub | BodyTransform AI", page_icon="💎", layout="wide")
apply_premium_theme()

# 2. Security Check
if not st.session_state.get('is_pro', False):
    st.warning("🔒 Premium Access Required. Please activate your key on the Diet Plan page.")
    if st.button("Go to Diet Plan"):
        st.switch_page("pages/2_Diet_Plan.py")
    st.stop()

# --- 3. THE SYNC ENGINE ---
day_count = st.session_state.get('program_day', 1)
diet_type = st.session_state.get('diet', 'Normal')
user_name = st.session_state.get('user_name', 'Champion')
client_id = st.session_state.get('client_id', 'BT-XXXXXX')
target_cal = st.session_state.get('target_calories', 2000)

variety_index = day_count % 3

if diet_type == "Vegan":
    proteins = ["Tofu", "Tempeh", "Seitan"]
elif diet_type == "Halal":
    proteins = ["Halal Chicken", "Halal Beef", "Halal Lamb"]
else:
    proteins = ["Chicken Breast", "Salmon Fillet", "Lean Beef"]

current_protein = proteins[variety_index]

# --- 4. RECIPE DATABASE ---
recipe_db = {
    "Chicken Breast": {"title": "Lemon Garlic Chicken",
                       "method": "Pan-sear with thyme and garlic for 6 mins per side."},
    "Salmon Fillet": {"title": "Omega-3 Baked Salmon",
                      "method": "Bake at 200°C for 12 mins with lemon slices and fresh dill."},
    "Lean Beef": {"title": "High-Iron Beef Sauté", "method": "Flash-fry beef strips on high heat with ginger."},
    "Halal Chicken": {"title": "Spiced Halal Chicken", "method": "Marinate in yogurt and cumin. Grill until charred."},
    "Halal Beef": {"title": "Savory Halal Steak", "method": "Sear in a hot skillet with rosemary and garlic."},
    "Halal Lamb": {"title": "Slow-Roasted Halal Lamb",
                   "method": "Season with mint and garlic. Slow roast until tender."},
    "Tofu": {"title": "Crispy Sesame Tofu", "method": "Air-fry at 200°C for 15 mins. Toss in soy sauce."},
    "Tempeh": {"title": "Balsamic Glazed Tempeh", "method": "Marinate in balsamic and pan-fry until sticky."},
    "Seitan": {"title": "Seitan Pepper Stir-fry", "method": "Stir-fry with bell peppers and onions."}
}

active_recipe = recipe_db[current_protein]


# --- 5. PROFESSIONAL PDF GENERATOR ---
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()

    # 1. Header Section
    pdf.set_fill_color(17, 17, 17)
    pdf.rect(0, 0, 210, 45, 'F')

    pdf.set_text_color(183, 228, 199)  # Mint Green
    pdf.set_font("Arial", "B", 26)
    pdf.cell(0, 20, txt="BODYTRANSFORM AI", ln=True, align='C')

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(0, 5, txt=f"PREMIUM PERFORMANCE PROTOCOL | DAY {day_count}", ln=True, align='C')
    pdf.ln(15)

    # 2. Client Profile Row
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(245, 245, 245)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(65, 12, txt=f" NAME: {user_name.upper()}", border=0, fill=True)
    pdf.cell(60, 12, txt=f" ID: {client_id}", border=0, fill=True)
    pdf.cell(65, 12, txt=f" CALORIES: {target_cal} KCAL", border=0, fill=True, align='R')
    pdf.ln(18)

    # 3. Macro Chart Visualization
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, txt="DAILY MACRONUTRIENT RATIOS", ln=True)

    # Protein Bar
    pdf.set_fill_color(183, 228, 199)
    pdf.rect(10, pdf.get_y(), 190, 7, 'F')
    pdf.set_font("Arial", "B", 8)
    pdf.text(12, pdf.get_y() + 5, f"PROTEIN: {int(target_cal * 0.3 / 4)}g")
    pdf.ln(10)

    # Carbs/Fats Bars
    pdf.set_fill_color(220, 220, 220)
    pdf.rect(10, pdf.get_y(), 150, 7, 'F')
    pdf.text(12, pdf.get_y() + 5, f"CARBS: {int(target_cal * 0.4 / 4)}g")
    pdf.ln(10)

    pdf.set_fill_color(240, 240, 240)
    pdf.rect(10, pdf.get_y(), 90, 7, 'F')
    pdf.text(12, pdf.get_y() + 5, f"FATS: {int(target_cal * 0.3 / 9)}g")
    pdf.ln(15)

    # 4. Recipe & Photo Box
    pdf.set_draw_color(183, 228, 199)
    pdf.rect(140, 105, 60, 50)
    pdf.set_font("Arial", "I", 8)
    pdf.text(148, 130, "Meal Photo Area")

    pdf.set_y(105)
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(46, 125, 50)
    pdf.cell(120, 10, txt=active_recipe['title'], ln=True)

    pdf.ln(3)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(120, 10, txt="INSTRUCTIONS:", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(125, 8, txt=active_recipe['method'])

    pdf.ln(10)

    # 5. DAILY SUCCESS CHECKLIST (New Feature)
    pdf.set_fill_color(240, 250, 240)
    pdf.rect(10, 175, 190, 60, 'F')
    pdf.set_y(180)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, txt="  DAILY PERFORMANCE CHECKLIST", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, txt="  [  ]  Hit Protein Goal", ln=True)
    pdf.cell(0, 8, txt="  [  ]  Consumed 3 Liters of Water", ln=True)
    pdf.cell(0, 8, txt="  [  ]  Stayed Within Calorie Target", ln=True)
    pdf.cell(0, 8, txt="  [  ]  Minimum 7-8 Hours Sleep", ln=True)
    pdf.cell(0, 8, txt="  [  ]  Completed Daily Movement / Workout", ln=True)

    # 6. Dark Footer
    pdf.set_y(-30)
    pdf.set_fill_color(17, 17, 17)
    pdf.rect(0, 270, 210, 30, 'F')
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", "I", 8)
    pdf.cell(0, 15, txt=f"Support: nassima.lagrini@gmail.com | Powered by BodyTransform AI", align='C')

    return bytes(pdf.output(dest='S'))


# --- 7. UI DISPLAY ---
st.title("💎 Elite Pro Recipe Hub")
st.success(f"✅ Ready for Day {day_count}: **{current_protein}**")

# Display the information on screen
c1, c2 = st.columns([2, 1])
with c1:
    st.header(active_recipe['title'])
    st.info(f"**Preparation:** {active_recipe['method']}")
with c2:
    st.markdown("### 📊 Metrics")
    st.write(f"Target: **{target_cal} kcal**")
    st.write(f"Protein: **{int(st.session_state['weight'] * 2)}g**")

st.write("---")
st.download_button(
    label="📥 DOWNLOAD PERFORMANCE PLAN (CHECKLIST INCLUDED)",
    data=generate_pdf(),
    file_name=f"Performance_Plan_Day_{day_count}.pdf",
    mime="application/pdf",
    use_container_width=True
)

if st.button("📊 Back to Dashboard", use_container_width=True):
    st.switch_page("pages/3_Dashboard.py")