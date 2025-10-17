import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import matplotlib.pyplot as plt
import json

st.set_page_config(page_title="2D Political Model", layout="centered")

st.title("🧭 The Political Model")
st.markdown(
    "Answer each question to find your position on the **Economic (X)** and **Social (Y)** axes."
)

# --- Load questions from JSON ---
with open("questions.json", "r") as f:
    questions = json.load(f)

options = {
    "Strongly Disagree": -2,
    "Disagree": -1,
    "Neutral": 0,
    "Agree": 1,
    "Strongly Agree": 2,
}

x_score, y_score = 0, 0
for q in questions:
    st.write(f"**{q['text']}**")
    choice = st.radio("", list(options.keys()), horizontal=True, key=q["text"])
    val = options[choice] * q["weight"]
    if q["axis"] == "x":
        x_score += val
    else:
        y_score += val

# --- Normalize to –1…+1 ---
max_x = sum(abs(q["weight"]) for q in questions if q["axis"] == "x") * 2
max_y = sum(abs(q["weight"]) for q in questions if q["axis"] == "y") * 2

x_norm = x_score / max_x
y_norm = y_score / max_y

st.subheader("📊 Your Coordinates")
st.write(f"**Economic (X):** {x_norm:.2f}  **Social (Y):** {y_norm:.2f}")

# --- Plot ---
fig, ax = plt.subplots(figsize=(6, 6))
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)

# Your point
ax.scatter(x_norm, y_norm, color="purple", s=120, label="You")

# Corner labels
ax.text(-1, -1, "Libertarian", ha="left", va="bottom", fontsize=10)
ax.text(1, -1, "Anarcho-Capitalist", ha="right", va="bottom", fontsize=10)
ax.text(-1, 1, "Communist", ha="left", va="top", fontsize=10)
ax.text(1, 1, "Fascist", ha="right", va="top", fontsize=10)

# Historical figures
figures = {
    "Thomas Jefferson": (0.4, -0.5),
    "Karl Marx": (-0.9, 0.8),
    "Benito Mussolini": (0.7, 0.9),
    "Milton Friedman": (0.8, -0.4)
}
for name, (x, y) in figures.items():
    ax.scatter(x, y, s=70, label=name)
    ax.text(x, y + 0.05, name, fontsize=8, ha="center")

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xlabel("Economic Axis (Left → Right)")
ax.set_ylabel("Social Axis (Libertarian → Authoritarian)")
ax.legend(loc="upper left", fontsize=7)
st.pyplot(fig)

st.markdown("---")
st.caption("Created with 🟣 **The Purple Initiative** — © 2025 Danny Krikorian")
st.set_page_config(
    
