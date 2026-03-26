# Monte Carlo Option Pricing Model

## Overview
This project implements a Monte Carlo simulation to price European call options using Geometric Brownian Motion.

## Features
- Simulation of asset price paths
- Option pricing via Monte Carlo
- Black–Scholes analytical pricing for comparison

## Technologies
- Python
- NumPy
- matplotlib

## How to Run
- python monte_carlo_option_pricing.py (for option pricing and Black-Scholes comparison)
- python geometric_brownian_motion.py (for simulation and plots of geometric BM)
- python one_dim_brownian_motion.py (for simulation and plots of 1D BM)

## Note on time
When asked how long each time increment should be and when the simulation should end, provide your answer in years.
If you want to assume the standard 252 training days in the year, then you would enter 0.004 for the increment.