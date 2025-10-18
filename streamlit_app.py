import streamlit as st
import matplotlib.pyplot as plt
import json
from adjustText import adjust_text   # prevents overlapping labels

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="The Political Model – The Purple Initiative",
    page_icon="🟣",
    layout="centered"
)

# --- TITLE ---
st.markdown(
    "<h1 style='text-align:center; color:#6A0DAD;'>🟣 The Political Model</h1>",
    unsafe_allow_html=True
)

st.markdown("""
Answer each question to find your position on the **Economic (Authority–Anarchy)** 
and **Social (Inclusion–Exclusion)** axes.
""")

# --- LOAD QUESTIONS ---
try:
    with open("questions.json", "r") as f:
        questions = json.load(f)
except FileNotFoundError:
    st.error("❌ Could not find 'questions.json'. Please make sure it's in the same folder as this file.")
    st.stop()

# --- ANSWER OPTIONS ---
options = {
    "Strongly Disagree": -2,
    "Disagree": -1,
    "Neutral": 0,
    "Agree": 1,
    "Strongly Agree": 2,
}

# --- SCORE CALCULATION ---
x_score, y_score = 0, 0
for q in questions:
    st.write(f"**{q['text']}**")
    choice = st.radio("", list(options.keys()), horizontal=True, key=q["text"])
    val = options[choice] * q["weight"]
    if q["axis"] == "x":
        x_score += val
    else:
        y_score += val

# --- NORMALIZE SCORES TO -1...+1 ---
max_x = sum(abs(q["weight"]) for q in questions if q["axis"] == "x") * 2
max_y = sum(abs(q["weight"]) for q in questions if q["axis"] == "y") * 2
x_norm = x_score / max_x if max_x != 0 else 0
y_norm = y_score / max_y if max_y != 0 else 0

# --- SHOW RESULTS ---
st.subheader("📊 Your Coordinates")
st.write(f"**Social (X - Inclusion → Exclusion):** {x_norm:.2f}")
st.write(f"**Economic (Y - Authority → Anarchy):** {y_norm:.2f}")

# --- PLOT RESULTS ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)

# User’s position
ax.scatter(x_norm, y_norm, color="#6A0DAD", s=120, label="You")

# --- CORNER LABELS ---
ax.text(-1, 1, "Authoritarian Inclusion\n(Communist / Theocratic)",
        ha="left", va="top", fontsize=9)
ax.text(1, 1, "Authoritarian Exclusion\n(Fascist / Nationalist)",
        ha="right", va="top", fontsize=9)
ax.text(-1, -1, "Anarchic Inclusion\n(Libertarian Socialist)",
        ha="left", va="bottom", fontsize=9)
ax.text(1, -1, "Anarchic Exclusion\n(Anarcho-Capitalist)",
        ha="right", va="bottom", fontsize=9)

# --- HISTORICAL FIGURES ---
figures = {
    "Thomas Jefferson": (0.3, -0.6),
    "Karl Marx": (-0.7, 0.8),
    "Benito Mussolini": (0.8, 0.9),
    "Milton Friedman": (0.6, -0.5)
}

texts = []
for name, (x, y) in figures.items():
    ax.scatter(x, y, s=70, label=name)
    txt = ax.text(x, y, name, fontsize=8, ha="center", va="center")
    texts.append(txt)

# Adjust text to prevent overlap
adjust_text(texts, arrowprops=dict(arrowstyle="-", color="gray", lw=0.5))

# --- AXES & LEGEND ---
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xlabel("Social Axis (Inclusion → Exclusion)")
ax.set_ylabel("Economic Axis (Authority → Anarchy)")
ax.legend(loc="upper left", fontsize=7)

st.pyplot(fig)

# --- FOOTER ---
st.markdown("---")
st.caption("Created with 🟣 **The Purple Initiative** — © 2025 Danny Krikorian")
