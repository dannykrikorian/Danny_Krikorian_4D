# --- PLOT RESULTS ---
from adjustText import adjust_text

fig, ax = plt.subplots(figsize=(6, 6))
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)

# User's position
ax.scatter(x_norm, y_norm, color="#6A0DAD", s=120, label="You")

# --- CORNER LABELS (NEW ORIENTATION) ---
ax.text(-1, 1, "Authoritarian Inclusion\n(Communist / Theocratic)",
        ha="left", va="top", fontsize=9)
ax.text(1, 1, "Authoritarian Exclusion\n(Fascist / Nationalist)",
        ha="right", va="top", fontsize=9)
ax.text(-1, -1, "Anarchic Inclusion\n(Libertarian Socialist)",
        ha="left", va="bottom", fontsize=9)
ax.text(1, -1, "Anarchic Exclusion\n(Anarcho-Capitalist)",
        ha="right", va="bottom", fontsize=9)

# --- HISTORICAL FIGURES (ADJUSTED COORDINATES) ---
figures = {
    "Thomas Jefferson": (0.3, -0.6),
    "Karl Marx": (-0.7, 0.8),
    "Benito Mussolini": (0.8, 0.9),
    "Milton Friedman": (0.6, -0.5),
    "You": (x_norm, y_norm)
}

# Plot all points and labels, then adjust
texts = []
for name, (x, y) in figures.items():
    ax.scatter(x, y, s=70, label=name if name != "You" else "")
    txt = ax.text(x, y, name, fontsize=8, ha="center", va="center")
    texts.append(txt)

adjust_text(texts, arrowprops=dict(arrowstyle="-", color="gray", lw=0.5))

# --- AXES & LEGEND ---
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xlabel("Social Axis (Inclusion → Exclusion)")
ax.set_ylabel("Economic Axis (Authority → Anarchy)")
ax.legend(loc="upper left", fontsize=7)
st.pyplot(fig)
