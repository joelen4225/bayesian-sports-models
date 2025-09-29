# Import the model and run inference
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the model components
from model import model, fit, theta_samples, y_rep_samples, N, wins, alpha_prior, beta_prior
import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("BAYESIAN BETA-BINOMIAL MODEL RESULTS")
print("=" * 60)

# Print model summary
print("\nMODEL SUMMARY:")
print(fit.summary())

print("\n" + "=" * 60)
print("PARAMETER ESTIMATES")
print("=" * 60)

# Calculate and display key statistics
theta_mean = np.mean(theta_samples)
theta_median = np.median(theta_samples)
theta_std = np.std(theta_samples)
theta_credible_interval = np.percentile(theta_samples, [2.5, 97.5])

print(f"Win Rate (Theta) Statistics:")
print(f"  Mean: {theta_mean:.4f}")
print(f"  Median: {theta_median:.4f}")
print(f"  Standard Deviation: {theta_std:.4f}")
print(f"  95% Credible Interval: [{theta_credible_interval[0]:.4f}, {theta_credible_interval[1]:.4f}]")

print(f"\nPrior Parameters:")
print(f"  Alpha: {alpha_prior}")
print(f"  Beta: {beta_prior}")

print(f"\nObserved Data:")
print(f"  Total Games: {N}")
print(f"  Wins: {wins}")
print(f"  Observed Win Rate: {wins/N:.4f}")

print("\n" + "=" * 60)
print("POSTERIOR PREDICTIVE CHECKS")
print("=" * 60)

# Posterior predictive statistics
y_rep_mean = np.mean(y_rep_samples)
y_rep_median = np.median(y_rep_samples)
y_rep_credible_interval = np.percentile(y_rep_samples, [2.5, 97.5])

print(f"Predicted Wins Statistics:")
print(f"  Mean Predicted Wins: {y_rep_mean:.2f}")
print(f"  Median Predicted Wins: {y_rep_median:.1f}")
print(f"  95% Credible Interval: [{y_rep_credible_interval[0]:.1f}, {y_rep_credible_interval[1]:.1f}]")

# Check if observed value is within credible interval
if y_rep_credible_interval[0] <= wins <= y_rep_credible_interval[1]:
    print(f"✓ Observed wins ({wins}) is within the 95% credible interval")
else:
    print(f"✗ Observed wins ({wins}) is outside the 95% credible interval")

print("\n" + "=" * 60)
print("VISUALIZATION")
print("=" * 60)

# Create comprehensive visualization
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Posterior distribution of theta
axes[0, 0].hist(theta_samples, bins=50, alpha=0.7, density=True, color='skyblue', edgecolor='black')
axes[0, 0].axvline(theta_mean, color='red', linestyle='--', linewidth=2, 
                   label=f'Mean: {theta_mean:.4f}')
axes[0, 0].axvline(theta_median, color='orange', linestyle=':', linewidth=2,
                   label=f'Median: {theta_median:.4f}')
axes[0, 0].axvline(wins/N, color='green', linestyle='-', linewidth=2,
                   label=f'Observed: {wins/N:.4f}')
axes[0, 0].set_xlabel('Win Rate (Theta)')
axes[0, 0].set_ylabel('Density')
axes[0, 0].set_title('Posterior Distribution of Win Rate')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Posterior predictive distribution
axes[0, 1].hist(y_rep_samples, bins=range(N+2), alpha=0.7, density=True, 
               color='lightgreen', edgecolor='black')
axes[0, 1].axvline(wins, color='red', linestyle='--', linewidth=2, 
                  label=f'Observed: {wins}')
axes[0, 1].axvline(y_rep_mean, color='blue', linestyle=':', linewidth=2,
                  label=f'Mean Predicted: {y_rep_mean:.1f}')
axes[0, 1].set_xlabel('Number of Wins')
axes[0, 1].set_ylabel('Density')
axes[0, 1].set_title('Posterior Predictive Distribution')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Trace plot for theta
axes[1, 0].plot(theta_samples, alpha=0.7)
axes[1, 0].set_xlabel('Iteration')
axes[1, 0].set_ylabel('Theta')
axes[1, 0].set_title('Trace Plot: Win Rate')
axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Autocorrelation
from scipy.stats import pearsonr
lags = range(1, min(50, len(theta_samples)//4))
autocorr = [pearsonr(theta_samples[:-lag], theta_samples[lag:])[0] for lag in lags]
axes[1, 1].plot(lags, autocorr, 'o-')
axes[1, 1].set_xlabel('Lag')
axes[1, 1].set_ylabel('Autocorrelation')
axes[1, 1].set_title('Autocorrelation Function')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("Visualization complete! Check the plots above for detailed analysis.")
print("\n" + "=" * 60)