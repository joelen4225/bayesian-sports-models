import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Define our posterior Beta distribution(10, 8)
    alpha = 10
    beta = 8

    # Number of simulations
    n_sim = 10000

    # Simulate theta from the posterior Beta distribution
    theta_sim = np.random.beta(alpha, beta, n_sim)

    # Simulate # of wins in the remaining 7 games
    remaining_wins_sim = np.random.binomial(7, theta_sim, n_sim)

    # Total wins, adding the already won 6 games
    total_wins_sim = 6 + remaining_wins_sim

    # Create a DataFrame for plotting
    total_wins_df = pd.DataFrame({'total_wins': total_wins_sim})

    # Plot the histogram of total wins simulated
    plt.figure(figsize=(10, 6))
    plt.hist(total_wins_df['total_wins'], bins=range(6, 15), 
             color='skyblue', edgecolor='black', alpha=0.7)
    plt.title('Histogram of Simulated Total Wins')
    plt.xlabel('Total Wins')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.show()
    
    return total_wins_sim


def run_simulation():
    """Function to run simulation and return total_wins_sim for import"""
    return main()


def get_simulation_data():
    """Function to get simulation data without plotting - for import use"""
    # Define our posterior Beta distribution(10, 8)
    alpha = 10
    beta = 8

    # Number of simulations
    n_sim = 10000

    # Simulate theta from the posterior Beta distribution
    theta_sim = np.random.beta(alpha, beta, n_sim)

    # Simulate # of wins in the remaining 7 games
    remaining_wins_sim = np.random.binomial(7, theta_sim, n_sim)

    # Total wins, adding the already won 6 games
    total_wins_sim = 6 + remaining_wins_sim
    
    return total_wins_sim


if __name__ == "__main__":
    main()