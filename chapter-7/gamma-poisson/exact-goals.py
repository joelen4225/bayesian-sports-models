import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import importlib.util
import sys
import os

# Import the simulating-data.py file (handling the hyphen in filename)
current_dir = os.path.dirname(os.path.abspath(__file__))
simulating_data_path = os.path.join(current_dir, "simulating-data.py")
spec = importlib.util.spec_from_file_location("simulating_data", simulating_data_path)
simulating_data = importlib.util.module_from_spec(spec)
sys.modules["simulating_data"] = simulating_data
spec.loader.exec_module(simulating_data)

def main():
    # Import the simulated future goals data (without plotting)
    future_goals_sim = simulating_data.get_simulation_data()
    
    # Probability that the team scores exactly 4 goals?
    prob_4_goals = np.mean(future_goals_sim == 4)
    print(f"Probability of exactly 4 goals: {prob_4_goals:.4f}")

    # Probability that the team scores exactly 5 goals?
    prob_10_goals = np.mean(future_goals_sim == 10)
    print(f"Probability of exactly 10 goals: {prob_10_goals:.4f}")

if __name__ == "__main__":
    main()
