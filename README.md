# Monte Carlo Investment Simulation

A Python project that models investment growth over time using Monte Carlo simulation and Geometric Brownian Motion (GBM). It generates thousands of possible future price paths to estimate potential outcomes, helping to analyse risk, return, and uncertainty in financial markets.

---

## Overview

This simulation assumes that asset prices evolve randomly but follow a general upward trend based on expected returns. By running many simulations, we can approximate the range of possible investment outcomes rather than relying on a single forecast.

It is commonly used in quantitative finance for:

* Risk analysis
* Portfolio modelling
* Option pricing foundations
* Scenario testing

---

## Model Used

The project uses **Geometric Brownian Motion (GBM)**:

* Expected return (drift): μ
* Volatility: σ
* Random market shocks: normally distributed noise

This produces realistic stochastic price movements over time.

---

## Features

* Runs thousands of simulated investment paths
* Models uncertainty in financial markets
* Uses daily time steps (252 trading days/year)
* Outputs key statistics:

  * Mean final value
  * Median outcome
  * 5% worst-case scenario (risk estimate)
  * 95% best-case scenario
* Visualises multiple simulated growth paths

---

## Technologies

* Python 3
* NumPy
* Matplotlib

---

## How to Run

### 1. Install dependencies

```bash
pip install numpy matplotlib
```

### 2. Run the simulation

```bash
python monte_carlo_simulation.py
```

---

## Parameters

You can adjust the model inside the script:

* `initial_investment` → starting capital
* `mu` → expected annual return
* `sigma` → volatility (risk level)
* `time_horizon` → investment duration (years)
* `num_simulations` → number of Monte Carlo runs

---

## Output

The program generates:

* A graph of simulated investment paths
* Summary statistics including:

  * Mean final value
  * Median final value
  * 5% and 95% percentile outcomes

---

## Learning Outcomes

This project demonstrates:

* Monte Carlo simulation techniques
* Stochastic modelling in finance
* Risk vs return analysis
* Practical application of GBM
* Python-based quantitative modelling

---

## Future Improvements

* Add monthly contributions (DCA strategy)
* Extend to multi-asset portfolios
* Include inflation adjustment
* Calculate Value at Risk (VaR)
* Build an interactive dashboard (Streamlit)

---

## Author

Rhys Barker-White
