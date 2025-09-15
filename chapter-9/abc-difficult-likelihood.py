# Load necessary library
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Observed data
n_at_bats_first_part = 81
observed_hits_first_part = 23
n_at_bats_second_part = 81
observed_hits_second_part = 12

# Total number of at-bats
n_at_bats_total = n_at_bats_first_part + n_at_bats_second_part

# Prior distribution parameters for theta1 and theta2
alpha_prior = 5
beta_prior = 25

# Number of simulations
n_sim = 10000

# Define a tolerance level for accepting simulated data
tolerance = 1

# Store accepted values of theta1, theta2, and Tc
accepted_theta1 = np.zeros(n_sim)
accepted_theta2 = np.zeros(n_sim)
accepted_theta_c = np.zeros(n_sim)

# ABC algorithm
np.random.seed(123)
count = 0
for i in range(n_sim):
    # Step 1: Simulate theta1 and theta2 from the prior
    theta1 = np.random.beta(alpha_prior, beta_prior)
    theta2 = np.random.beta(alpha_prior, beta_prior)

    # Step 2: Simulate a change point Tc
    Tc = np.random.randint(1, n_at_bats_total)

    # Step 3: Simulate hits
    sim_hits1 = np.random.binomial(Tc, theta1)
    sim_hits2 = np.random.binomial(n_at_bats_total - Tc, theta2)

    # Step 4: Compare simulated hits to observed hits
    if (abs(sim_hits1 - observed_hits_first_part) <= tolerance and abs(sim_hits2 - observed_hits_second_part) <= tolerance):
        accepted_theta1[count] = theta1
        accepted_theta2[count] = theta2
        accepted_theta_c[count] = Tc
        count += 1

# Remove zeros (rejected samples)
accepted_theta1 = accepted_theta1[accepted_theta1 > 0]
accepted_theta2 = accepted_theta2[accepted_theta2 > 0]
accepted_Tc = accepted_theta_c[accepted_theta_c > 0]

# Plot the approximate posterior distribution
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.hist(accepted_theta1, bins=30, density=True, alpha=0.7, color='blue')
plt.title('Posterior of Batting Average Before Injury')
plt.xlabel('θ₁')
plt.ylabel('Density')
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 2)
plt.hist(accepted_theta2, bins=30, density=True, alpha=0.7, color='blue')
plt.title('Posterior of Batting Average After Injury')
plt.xlabel('θ₂')
plt.ylabel('Density')
plt.grid(True, alpha=0.3)

# Calculate the mean and credible interval
mean_theta1 = np.mean(accepted_theta1)
credible_interval_theta1 = np.quantile(accepted_theta1, [0.025, 0.975])

mean_theta2 = np.mean(accepted_theta2)
credible_interval_theta2 = np.quantile(accepted_theta2, [0.025, 0.975])

mean_Tc = np.mean(accepted_Tc)
credible_interval_Tc = np.quantile(accepted_Tc, [0.025, 0.975])

print("Mean θ₁:", mean_theta1)
print("95% Credible Interval θ₁:", credible_interval_theta1)

print("Mean θ₂:", mean_theta2)
print("95% Credible Interval θ₂:", credible_interval_theta2)

print("Mean Tc:", mean_Tc)
print("95% Credible Interval Tc:", credible_interval_Tc)

# Plot the combined distributions
combined_theta = np.concatenate([accepted_theta1, accepted_theta2])
combined_period = ['Before Injury'] * len(accepted_theta1) + ['After Injury'] * len(accepted_theta2)

plt.subplot(2, 2, 3)
plt.hist([accepted_theta1, accepted_theta2], bins=30, density=True, alpha=0.5, 
         label=['Before Injury', 'After Injury'], color=['blue', 'green'])
plt.title('Posterior Distributions')
plt.xlabel('θ')
plt.ylabel('Density')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot the posterior distribution of change point
plt.subplot(2, 2, 4)
plt.hist(accepted_Tc, bins=30, density=True, alpha=0.7, color='red')
plt.title('Posterior of Change Point')
plt.xlabel('Tc')
plt.ylabel('Density')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

