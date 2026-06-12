#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:37:51 2026

@author: rhysbarker-white
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Inputs
# ----------------------------
initial_investment = 10000   # starting amount (£/$)
mu = 0.07                    # expected annual return (7%)
sigma = 0.15                 # volatility (15%)
time_horizon = 10            # years
num_simulations = 1000       # number of Monte Carlo paths
steps_per_year = 252        # trading days

dt = 1 / steps_per_year

# ----------------------------
# Simulation
# ----------------------------
num_steps = time_horizon * steps_per_year

results = np.zeros((num_simulations, num_steps))

for i in range(num_simulations):
    prices = np.zeros(num_steps)
    prices[0] = initial_investment

    for t in range(1, num_steps):
        random_shock = np.random.normal(0, 1)
        
        # Geometric Brownian Motion
        prices[t] = prices[t-1] * np.exp(
            (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * random_shock
        )
    
    results[i] = prices

# ----------------------------
# Plot sample paths
# ----------------------------
plt.figure(figsize=(12,6))

for i in range(20):  # plot 20 random paths
    plt.plot(results[i], linewidth=1)

plt.title("Monte Carlo Simulation of Investment Growth")
plt.xlabel("Time (Days)")
plt.ylabel("Portfolio Value")
plt.show()

# ----------------------------
# Final distribution
# ----------------------------
final_values = results[:, -1]

print("Mean final value:", np.mean(final_values))
print("Median final value:", np.median(final_values))
print("5% worst case:", np.percentile(final_values, 5))
print("5% best case:", np.percentile(final_values, 95))