import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd

from simulation import run_simulation

st.set_page_config(page_title="Monte Carlo Risk Simulator", layout="wide")

st.title("🎲 Monte Carlo Risk Simulator")

st.markdown(
    "Simulate possible future portfolio outcomes using probabilistic modeling."
)

# -------------------------
# SCENARIO SYSTEM
# -------------------------
st.sidebar.header("Scenario Presets")

scenario = st.sidebar.selectbox(
    "Choose Risk Scenario",
    ["Custom", "Low Risk", "Medium Risk", "High Risk"]
)

scenario_map = {
    "Low Risk": {"mean": 0.01, "vol": 0.03},
    "Medium Risk": {"mean": 0.02, "vol": 0.05},
    "High Risk": {"mean": 0.04, "vol": 0.10},
}

# -------------------------
# INPUTS
# -------------------------
initial = st.sidebar.number_input("Initial Investment", value=10000)

months = st.sidebar.slider("Months", 6, 120, 24)
sims = st.sidebar.slider("Simulations", 100, 500, 200)

# scenario override logic
if scenario == "Custom":
    mean_return = st.sidebar.slider("Expected Monthly Return (%)", -5.0, 10.0, 2.0) / 100
    volatility = st.sidebar.slider("Volatility (%)", 1.0, 20.0, 5.0) / 100
else:
    mean_return = scenario_map[scenario]["mean"]
    volatility = scenario_map[scenario]["vol"]

# -------------------------
# RUN SIMULATION
# -------------------------
results = run_simulation(
    initial,
    mean_return,
    volatility,
    months,
    sims
)

# -------------------------
# SIMULATION PATHS
# -------------------------
st.subheader("📈 Simulation Paths")

fig = go.Figure()

for i in range(min(50, sims)):
    fig.add_trace(
        go.Scatter(
            y=results[i],
            mode="lines",
            line=dict(width=1),
            opacity=0.3,
            showlegend=False
        )
    )

fig.update_layout(height=500)

st.plotly_chart(fig, use_container_width=True)

# -------------------------
# DISTRIBUTION
# -------------------------
st.subheader("📊 Final Value Distribution")

final_values = results[:, -1]

hist_fig = go.Figure(
    data=[go.Histogram(x=final_values, nbinsx=30)]
)

st.plotly_chart(hist_fig, use_container_width=True)

# -------------------------
# METRICS
# -------------------------
st.subheader("📌 Risk Metrics")

mean_value = np.mean(final_values)
best_case = np.max(final_values)
worst_case = np.min(final_values)

confidence_low = np.percentile(final_values, 2.5)
confidence_high = np.percentile(final_values, 97.5)

prob_double = np.mean(final_values > 2 * initial)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Average Outcome", f"${mean_value:,.0f}")
col2.metric("Best Case", f"${best_case:,.0f}")
col3.metric("Worst Case", f"${worst_case:,.0f}")
col4.metric("95% CI", f"${confidence_low:,.0f} - ${confidence_high:,.0f}")

st.metric("📈 Probability of Doubling Money", f"{prob_double*100:.2f}%")

# -------------------------
# DOWNLOAD DATA
# -------------------------
st.subheader("⬇️ Download Simulation Data")

df = pd.DataFrame(results.T)
df.columns = [f"Sim_{i}" for i in range(sims)]

csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="monte_carlo_results.csv",
    mime="text/csv"
)