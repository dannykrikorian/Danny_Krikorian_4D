import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Political Model Test", page_icon="📊", layout="centered")

st.title("🧭 The Political Model Test")
st.write("""
This model maps ideology across **two core dimensions**:

**Social (X-axis: Inclusion → Exclusion)**  
**Economic (Y-axis: Authority → Anarchy)**  

Your answers determine where you fall in relation to key public figures and ideological poles.
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
# SCALE
# ─────────────────────────────
options = {
    "Strongly Agree": 2,
    "Agree": 1,
    "Neutral": 0,
    "Disagree": -1,
    "Strongly Disagree": -2
}

# ─────────────────────────────
# SOCIAL SECTION
# ─────────────────────────────
st.header("🌐 Social Dimension (Inclusion → Exclusion)")
social_total = 0
for q in social_questions:
    choice = st.radio(q, list(options.keys()), index=2, key=q)
    social_total += options[choice]
social_score = social_total / len(social_questions)

# ─────────────────────────────
# ECONOMIC SECTION
# ─────────────────────────────
st.header("⚙️ Economic Dimension (Authority → Anarchy)")
economic_total = 0
for q in economic_questions:
    choice = st.radio(q, list(options.keys()), index=2, key=q)
    economic_total += options[choice]
economic_score = economic_total / len(economic_questions)

# ─────────────────────────────
# RESULTS
# ─────────────────────────────
st.subheader("📈 Your Coordinates")
st.write(f"**Social (X - Inclusion → Exclusion):** {social_score:.2f}")
st.write(f"**Economic (Y - Authority → Anarchy):** {economic_score:.2f}")

# ─────────────────────────────
# PLOT
# ─────────────────────────────
fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Grid lines and axes
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(0, color='gray', linewidth=0.8)

# Axis labels
ax.set_xlabel("Social: Inclusion → Exclusion")
ax.set_ylabel("Economic: Authority → Anarchy")

# Quadrant labels
ax.text(-1.8, 1.7, "Communism", color='red', fontsize=11, fontweight='bold')
ax.text(1.2, 1.7, "Fascism", color='gold', fontsize=11, fontweight='bold')
ax.text(-1.8, -1.8, "Libertarian", color='green', fontsize=11, fontweight='bold')
ax.text(1.0, -1.8, "Anarcho-Capitalist", color='orange', fontsize=11, fontweight='bold')

# Reference political figures
# (X = Social inclusion→exclusion, Y = Authority→anarchy)
references = {
    "AOC": (-1.3, -0.8),
    "Obama": (-0.5, -0.3),
    "Biden": (-0.2, 0.0),
    "Trump": (1.0, 0.3),
    "Thomas Massie": (1.2, -1.2)
}

for name, (x, y) in references.items():
    ax.scatter(x, y, color='white', s=60, edgecolors='black', zorder=5)
    ax.text(x + 0.05, y + 0.05, name, color='white', fontsize=10, fontweight='bold')

# User point
ax.scatter(social_score, economic_score, color='red', s=100, zorder=6)
ax.text(social_score + 0.08, economic_score + 0.08, "You", color='white', fontsize=12, fontweight='bold')

# Dark theme adjustments
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
    st.write("""
You align with **Inclusive-Anarchic** tendencies —  
valuing diversity, mutual aid, and individual freedom over hierarchy.  
This quadrant represents decentralized, egalitarian, and libertarian-left ideals.
""")
elif social_score > 0 and economic_score < 0:
    st.write("""
You align with **Exclusive-Anarchic** tendencies —  
emphasizing independence, minimal government, and skepticism toward outsiders.  
Typically associated with right-libertarian or market-individualist schools.
""")
elif social_score < 0 and economic_score > 0:
    st.write("""
You align with **Inclusive-Authoritarian** tendencies —  
favoring social equality and state intervention to protect the common good.  
This includes progressive socialists and regulated-welfare models.
""")
elif social_score > 0 and economic_score > 0:
    st.write("""
You align with **Exclusive-Authoritarian** tendencies —  
prioritizing order, hierarchy, nationalism, and centralized authority.  
Historically linked to nationalist or corporatist movements.
""")
else:
    st.write("""
You appear **Centrally balanced** —  
valuing both cooperation and structure, freedom and responsibility.  
This reflects pragmatic moderation or mixed-economy democracy.
""")
