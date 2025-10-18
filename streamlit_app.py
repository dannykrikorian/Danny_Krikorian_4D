import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Political Model Test", page_icon="📊", layout="centered")

st.title("🧭 The Political Model Test")
st.write("""
This model maps ideology across **two major dimensions** —  
**Social (Inclusion → Exclusion)** and **Economic (Authority → Anarchy)**.  
Answer each statement honestly from **Strongly Agree** to **Strongly Disagree**.
""")

# ─────────────────────────────
# QUESTIONS
# ─────────────────────────────
social_questions = [
    "Immigration strengthens a nation's culture.",
    "Religion should have no role in politics.",
    "Patriotism is often used to manipulate people.",
    "People of different backgrounds should mix freely.",
    "Tradition should guide social norms."
]

economic_questions = [
    "The state should control key industries.",
    "Taxes should be higher for the wealthy.",
    "Free markets produce fair outcomes.",
    "Unions are essential to protect workers.",
    "Government surveillance is justified to maintain order."
]

# ─────────────────────────────
# RESPONSE SCALE
# ─────────────────────────────
options = {
    "Strongly Agree": 2,
    "Agree": 1,
    "Neutral": 0,
    "Disagree": -1,
    "Strongly Disagree": -2
}

# ─────────────────────────────
# SOCIAL DIMENSION
# ─────────────────────────────
st.header("🌐 Social Dimension (Inclusion → Exclusion)")
social_total = 0
for q in social_questions:
    choice = st.radio(q, list(options.keys()), index=2, key=q)
    social_total += options[choice]

# Normalize (divide by number of questions)
social_score = social_total / len(social_questions)

# ─────────────────────────────
# ECONOMIC DIMENSION
# ─────────────────────────────
st.header("⚙️ Economic Dimension (Authority → Anarchy)")
economic_total = 0
for q in economic_questions:
    choice = st.radio(q, list(options.keys()), index=2, key=q)
    economic_total += options[choice]

economic_score = economic_total / len(economic_questions)

# ─────────────────────────────
# FINAL OUTPUT
# ─────────────────────────────
st.subheader("📈 Your Coordinates")
st.write(f"**Social (X - Inclusion → Exclusion):** {social_score:.2f}")
st.write(f"**Economic (Y - Authority → Anarchy):** {economic_score:.2f}")

# ─────────────────────────────
# COORDINATE PLOT
# ─────────────────────────────
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(0, color='gray', linewidth=0.8)
ax.set_xlabel("Social: Inclusion → Exclusion")
ax.set_ylabel("Economic: Authority → Anarchy")

# Plot the user coordinate
ax.scatter(social_score, economic_score, color='red', s=100, zorder=5)
ax.text(social_score + 0.1, economic_score + 0.1, "You", color='white', fontsize=12, fontweight='bold')

# Dark theme
ax.set_facecolor("#0e1117")
fig.patch.set_facecolor("#0e1117")
ax.tick_params(colors='white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

st.pyplot(fig)

# ─────────────────────────────
# INTERPRETATION
# ─────────────────────────────
st.markdown("### 🧩 Interpretation")
if social_score < 0 and economic_score < 0:
    st.write("You lean toward **inclusive authority** — valuing equality and social welfare with structured governance.")
elif social_score > 0 and economic_score < 0:
    st.write("You lean toward **exclusive authority** — valuing order, hierarchy, and tradition.")
elif social_score < 0 and economic_score > 0:
    st.write("You lean toward **inclusive anarchy** — emphasizing individual freedom and multiculturalism.")
elif social_score > 0 and economic_score > 0:
    st.write("You lean toward **exclusive anarchy** — emphasizing freedom for the self, independence, and skepticism of outsiders.")
else:
    st.write("You appear **centrist** — balanced between inclusion and exclusion, authority and liberty.")
