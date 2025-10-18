import streamlit as st
import matplotlib.pyplot as plt

# Example coordinates (replace with dynamic variables)
x = 0.00  # Social (Inclusion → Exclusion)
y = 1.00  # Economic (Authority → Anarchy)

st.header("📊 Your Coordinates")
st.write(f"**Social (X - Inclusion → Exclusion):** {x:.2f}")
st.write(f"**Economic (Y - Authority → Anarchy):** {y:.2f}")

# Create figure and plot
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(0, color='gray', linewidth=0.8)

# Labels for axes
ax.set_xlabel("Social: Inclusion → Exclusion")
ax.set_ylabel("Economic: Authority → Anarchy")

# Plot the user point
ax.scatter(x, y, color='red', s=100, zorder=5)
ax.text(x + 0.02, y + 0.02, "You", color='white', fontsize=12, fontweight='bold')

# Dark theme adjustment
ax.set_facecolor("#0e1117")
fig.patch.set_facecolor("#0e1117")
ax.tick_params(colors='white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')

# Render in Streamlit
st.pyplot(fig)
