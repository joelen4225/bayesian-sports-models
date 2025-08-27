import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import importlib.util
import sys
import os
from scipy.stats import gaussian_kde

# Import the simulating-data.py file (handling the hyphen in filename)
current_dir = os.path.dirname(os.path.abspath(__file__))
simulating_data_path = os.path.join(current_dir, "simulating-data.py")
spec = importlib.util.spec_from_file_location("simulating_data", simulating_data_path)
simulating_data = importlib.util.module_from_spec(spec)
sys.modules["simulating_data"] = simulating_data
spec.loader.exec_module(simulating_data)

def main():

    # Import the simulated future goals data (without plotting)
    lambda_sim = simulating_data.get_lambda_sim()

    # Create kernel density estimate
    kde = gaussian_kde(lambda_sim)
    
    # Create a fine grid of x values to evaluate the density
    x_grid = np.linspace(lambda_sim.min(), lambda_sim.max(), 1000)
    density_values = kde(x_grid)
    
    # Find the x value where density is maximum (MAP estimate)
    lambda_map = x_grid[np.argmax(density_values)]
    
    print(f"Maximum a posteriori estimate of lambda: {lambda_map:.4f}")
    


if __name__ == "__main__":
    main()