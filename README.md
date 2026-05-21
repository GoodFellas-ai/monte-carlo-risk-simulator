 # 🎲📄 Monte Carlo Risk Simulator

A probabilistic data science application that models future portfolio outcomes under uncertainty using Monte Carlo simulation techniques.

---

## 🎯 Project Objective

This project simulates possible future outcomes of an investment portfolio using stochastic modeling.

Instead of producing a single prediction, the system generates a **distribution of possible outcomes**, enabling risk-aware decision making.

The goal is to demonstrate **probabilistic thinking**, not deterministic prediction.

---

## 🧠 Core Idea

Financial markets are uncertain.

Instead of asking:
> “What will my portfolio be worth?”

This project answers:
> “What is the range of possible outcomes, and how likely are they?”

---

## 📊 Data Science Concepts Used

### 📌 1. Stochastic Simulation
- Monte Carlo simulation
- Random sampling from normal distribution
- Path-dependent portfolio evolution

### 📌 2. Probability Modeling
- Expected value estimation
- Distribution of outcomes
- Risk quantification

### 📌 3. Statistical Analysis
- Mean outcome
- Best/worst case scenarios
- Confidence intervals (95%)

### 📌 4. Risk Metrics
- Probability of doubling investment
- Outcome dispersion
- Tail risk analysis

---


## 🧮 Mathematical Model

Each step of the simulation follows:

$$
# P_t = P_{t-1} \times (1 + r_t)
$$

Where:

$$
# r_t \sim \mathcal{N}(\mu, \sigma)
$$

- \( P_t \): Portfolio value at time \( t \)  
- \( r_t \): Random return at time \( t \)  
- \( \mu \): Mean return  
- \( \sigma \): Volatility (risk)

This creates a stochastic growth process over time.

---

## ⚙️ Features

- 🎯 Scenario-based simulation (Low / Medium / High / Custom risk)
- 📈 Monte Carlo trajectory visualization
- 📊 Outcome distribution analysis
- 📌 Risk metrics dashboard
- 📈 Probability of doubling investment
- ⬇️ CSV export of simulation results

---

## 🛠️ Tech Stack

- Python
- NumPy (simulation engine)
- Pandas (data handling)
- Plotly (visualization)
- Streamlit (interactive dashboard)

---

## 🏗️ System Architecture


User Inputs (Scenario / Parameters)
↓
Monte Carlo Simulation Engine
↓
Stochastic Path Generation
↓
Statistical Aggregation Layer
↓
Visualization Dashboard (Streamlit)


---

## 📈 Outputs

The system produces:

- Multiple simulated portfolio trajectories
- Final value distribution
- Risk statistics (mean, min, max)
- Confidence intervals
- Probability metrics

---

## 🚀 How to Run Locally

bash

pip install -r requirements.txt
streamlit run app.py
📦 Requirements
streamlit
numpy
pandas
plotly

🌐 Deployment

Deployable via:

Render
Streamlit Cloud

Start command:

streamlit run app.py --server.port $PORT --server.address 0.0.0.0
📌 Project Type Classification

✔ Data Science (probabilistic modeling)
✔ Statistical simulation system
✔ Financial risk analytics tool

❌ Not a machine learning model
❌ No training / inference pipeline

## 🧠 Key Learning Outcomes
Monte Carlo simulation techniques
Uncertainty modeling
Risk quantification
Data visualization of stochastic systems
Building interactive analytics applications


🌐 Live Demo

https://monte-carlo-risk-simulator.onrender.com/
---

👤 Author

Data Science / Quantitative Analytics Project
