import streamlit as st
import plotly.graph_objects as go

st.markdown(
    """
    # The Purple Initiative Compass
    Explore a 4D slice of our 8D ideology model: **Inclusion ↔ Exclusion** (X) and **Anarchy ↔ Authority** (Y).
    Move the sliders to plot your position and compare with historical figures and movements.
    """,
)
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
import streamlit as st
st.set_page_config(
    page_title="The Purple Initiative Compass",
    page_icon="🧭",
    layout="wide"
)
APP_URL = "https://YOUR-APP-NAME.streamlit.app"  # replace

st.code(APP_URL, language=None)  # easy copy

st.markdown(
    f"""
    [Share on X](https://twitter.com/intent/tweet?text=Try%20this%20political%20compass&url={APP_URL}) ·
    [Share on Threads](https://www.threads.net/intent/post?text=Try%20this%20political%20compass%20{APP_URL}) ·
    [Share on Facebook](https://www.facebook.com/sharer/sharer.php?u={APP_URL})
    """,
    unsafe_allow_html=True
)
