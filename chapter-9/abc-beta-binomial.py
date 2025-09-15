# Load necessary library
import numpy as np
import matplotlib.pyplot as plt

# Define the prior distribution parameters
alpha_prior = 4
beta_prior = 4

# Observed data
n_games = 10
observed_wins = 6

# Number of simulations 
n_sim = 10000

# Define a tolerance level for accepting simulated data
# 0 games for an exact match of our observed data
tolerance = 0

# Store accepted values of theta
accepted_theta = np.zeros(n_sim)

# ABC algorithm
np.random.seed(123)
for i in range(n_sim):
    # Step 1: Simulate theta from the prior distribution
    theta = np.random.beta(alpha_prior, beta_prior)

    # Step 2: Simulate wins based on theta
    sim_wins = np.random.binomial(n_games, theta)

    # Step 3: Compare simulated wins to observed wins
    if abs(sim_wins - observed_wins) <= tolerance:
        accepted_theta[i] = theta

# Remove zeros (rejected samples)
accepted_theta = accepted_theta[accepted_theta > 0]

# Plot the approximate posterior distribution
plt.figure(figsize=(8, 6))
plt.hist(accepted_theta, bins=30, density=True, alpha=0.7, color='blue')
plt.xlabel('Win Rate')
plt.ylabel('Density')
plt.title('Approximate Posterior Distribution')
plt.grid(True, alpha=0.3)
plt.show()

print("Median:", np.median(accepted_theta))
print("95% Credible Interval:", np.quantile(accepted_theta, [0.025, 0.975]))

