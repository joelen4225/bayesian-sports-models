import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Define our posterior Gamma distribution(30, 9)
    shape = 30
    rate = 9

    # Number of simulations
    n_sim = 10000

    # Simulate lambda from the posterior Gamma distribution
    lambda_sim = np.random.gamma(shape, 1/rate, n_sim)  # Note: numpy uses scale=1/rate

    # Simulate # of goals in future games
    future_goals_sim = np.random.poisson(lambda_sim, n_sim)

    # Create a DataFrame for plotting
    future_goals_df = pd.DataFrame({'future_goals': future_goals_sim})

    # Plot the histogram of future goals
    plt.figure(figsize=(10, 6))
    # Use appropriate bins based on the data range
    max_goals = int(future_goals_df['future_goals'].max()) + 1
    plt.hist(future_goals_df['future_goals'], bins=range(0, max_goals + 1), 
             color='skyblue', edgecolor='black', alpha=0.7)
    plt.title('Histogram of Simulated Future Goals')
    plt.xlabel('Future Goals')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.show()
    
    return future_goals_sim


def run_simulation():
    """Function to run simulation and return total_wins_sim for import"""
    return main()

def get_lambda_sim():
    """Function to get simulation data without plotting - for import use"""
    # Define our posterior Gamma distribution(30, 9)
    shape = 30
    rate = 9

    # Number of simulations
    n_sim = 10000

    # Simulate lambda from the posterior Gamma distribution
    lambda_sim = np.random.gamma(shape, 1/rate, n_sim)  # Note: numpy uses scale=1/rate

    return lambda_sim

def get_simulation_data():
    """Function to get simulation data without plotting - for import use"""
    # Define our posterior Gamma distribution(30, 9)
    shape = 30
    rate = 9

    # Number of simulations
    n_sim = 10000

    # Simulate lambda from the posterior Gamma distribution
    lambda_sim = np.random.gamma(shape, 1/rate, n_sim)  # Note: numpy uses scale=1/rate

    # Simulate # of goals in future games
    future_goals_sim = np.random.poisson(lambda_sim, n_sim)
    
    return future_goals_sim


if __name__ == "__main__":
    main()