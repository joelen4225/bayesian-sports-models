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

    # Probability that the team wins more than 9.5 games?
    prob_more_than_9_5 = np.mean(total_wins_sim > 9.5)
    print(f"Probability of winning over 9.5 games: {prob_more_than_9_5:.4f}")

    # Probability that the team wins less than 9.5 games?
    prob_less_than_9_5 = 1 - prob_more_than_9_5
    print(f"Probability of winning less than 9.5 games: {prob_less_than_9_5:.4f}")

if __name__ == "__main__":
    main()