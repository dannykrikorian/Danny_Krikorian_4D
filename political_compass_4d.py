import streamlit as st
import plotly.graph_objects as go

st.title("4D Political Compass (Authority–Anarchy vs Inclusion–Exclusion)")

st.subheader("Set your position")
x_inclusion_exclusion = st.slider("Inclusion (Left) ↔ Exclusion (Right)", -10, 10, 0)
y_anarchy_authority = st.slider("Anarchy (Bottom) ↔ Authority (Top)", -10, 10, 0)

figures = {
    "Murray Bookchin": (-8, -6),
    "Thomas Jefferson": (-6, -4),
    "Vladimir Lenin": (2, 8),
    "Benito Mussolini": (8, 9),
    "Donald Trump": (6, 7),
    "Rojava (SDF)": (-7, -8),
    "Benjamin Netanyahu": (8, 8),
    "Your Position": (x_inclusion_exclusion, y_anarchy_authority),
}

fig = go.Figure()

# axes lines
fig.add_hline(y=0)
fig.add_vline(x=0)

# points
for name, (x, y) in figures.items():
    fig.add_trace(go.Scatter(
        x=[x], y=[y],
        mode="markers+text",
        text=[name],
        textposition="top center",
        marker=dict(size=14 if name=="Your Position" else 10,
                    color="red" if name=="Your Position" else "blue")
    ))

fig.update_layout(
    xaxis=dict(title="Inclusion (←) ↔ Exclusion (→)", range=[-10, 10], zeroline=False),
    yaxis=dict(title="Anarchy (↓) ↔ Authority (↑)", range=[-10, 10], zeroline=False),
    height=700, width=700, title="Authority–Anarchy vs Inclusion–Exclusion",
)

st.plotly_chart(fig, use_container_width=True)
