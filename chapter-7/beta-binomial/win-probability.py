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
    # Import the simulated total wins data (without plotting)
    total_wins_sim = simulating_data.get_simulation_data()
    
    # Probability that the team's win percentage is over 70%?
    prob_over_70 = np.mean(total_wins_sim / 17 > 0.7)
    print(f"Probability of win percentage over 70%: {prob_over_70:.4f}")

    # Probability that the team's win percentage is under 50%?
    prob_under_50 = np.mean(total_wins_sim / 17 < 0.5)
    print(f"Probability of win percentage under 50%: {prob_under_50:.4f}")

if __name__ == "__main__":
    main()