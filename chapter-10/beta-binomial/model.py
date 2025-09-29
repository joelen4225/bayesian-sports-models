# Load necessary libraries
import cmdstanpy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Define the data
N = 10
wins = 6
alpha_prior = 4
beta_prior = 4

data_dict = {
    'N': N, 
    'wins': wins, 
    'alpha': alpha_prior, 
    'beta': beta_prior
}

# Compile and run the Stan model
model = cmdstanpy.CmdStanModel(stan_file="model-definition.stan")
fit = model.sample(data=data_dict, 
                   iter_sampling=1000, 
                   iter_warmup=500,
                   chains=4,
                   seed=123)

# Print summary
print(fit)

# Extract posterior samples for theta
theta_samples = fit.stan_variable('theta')

# Calculate median
theta_median = np.median(theta_samples)

# Calculate 95% credible interval
theta_credible_interval = np.percentile(theta_samples, [2.5, 97.5])

# Print median and credible interval
print(f"Median: {theta_median:.4f}")
print(f"95% Credible Interval: [{theta_credible_interval[0]:.4f}, {theta_credible_interval[1]:.4f}]")

# Plot posterior distribution of theta
plt.figure(figsize=(10, 6))
plt.hist(theta_samples, bins=50, alpha=0.7, density=True, color='skyblue', edgecolor='black')
plt.axvline(theta_median, color='red', linestyle='--', linewidth=2, 
            label=f'Median: {theta_median:.4f}')
plt.axvline(theta_credible_interval[0], color='orange', linestyle=':', linewidth=2,
            label=f'95% CI: [{theta_credible_interval[0]:.4f}, {theta_credible_interval[1]:.4f}]')
plt.axvline(theta_credible_interval[1], color='orange', linestyle=':', linewidth=2)
plt.xlabel('Win Rate (Theta)')
plt.ylabel('Density')
plt.title('Posterior Distribution of Win Rate (Theta)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Additional analysis: Extract y_rep samples for posterior predictive checks
y_rep_samples = fit.stan_variable('y_rep')

# Plot posterior predictive distribution
plt.figure(figsize=(10, 6))
plt.hist(y_rep_samples, bins=range(N+2), alpha=0.7, density=True, 
         color='lightgreen', edgecolor='black')
plt.axvline(wins, color='red', linestyle='--', linewidth=2, 
            label=f'Observed: {wins}')
plt.xlabel('Number of Wins')
plt.ylabel('Density')
plt.title('Posterior Predictive Distribution')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Make variables available for import
if __name__ == "__main__":
    # Variables are already defined above
    pass