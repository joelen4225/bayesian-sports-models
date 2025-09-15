import numpy as np
import matplotlib.pyplot as plt

# Beta-Binomial Model Example
# Simulate Beta (10, 8) posterior distribution
alpha = 10
beta = 8
n_sim = 10000
theta_sim = np.random.beta(alpha, beta, n_sim)

# Calculate 95% credible interval
credible_interval_beta = np.percentile(theta_sim, [2.5, 97.5])
mean_credible_beta = np.mean(theta_sim)

# Observed data for the frequentist confidence interval
n = 10
x = 6
theta_mle = x / n
se_theta = np.sqrt(theta_mle * (1 - theta_mle) / n)
conf_interval_beta = [theta_mle - 1.96 * se_theta, theta_mle + 1.96 * se_theta]
mean_conf_beta = theta_mle

# True range
true_range = [0.3529, 0.764]

# Create the plot
fig, ax = plt.subplots(figsize=(6, 10))

# Plot the three intervals
x_positions = [3, 2, 1]  
intervals = [true_range, conf_interval_beta, credible_interval_beta]
means = [np.mean(true_range), mean_conf_beta, mean_credible_beta]
labels = ['True Range', 'Frequentist', 'Bayesian']

for i, (interval, mean, label) in enumerate(zip(intervals, means, labels)):
    # Plot the interval as a vertical black line
    ax.plot([x_positions[i], x_positions[i]], interval, color='black', linewidth=3)
    
    # Plot the min as a blue dot
    ax.plot(x_positions[i], interval[0], 'o', color='blue', markersize=8)
    
    # Plot the mean as a green dot
    ax.plot(x_positions[i], mean, 'o', color='green', markersize=8)
    
    # Plot the max as a red dot
    ax.plot(x_positions[i], interval[1], 'o', color='red', markersize=8)
    
    # Add text labels for the interval bounds
    ax.text(x_positions[i] - 0.1, interval[0], f'{interval[0]:.3f}', 
            ha='right', va='center', fontsize=9)
    ax.text(x_positions[i] - 0.1, interval[1], f'{interval[1]:.3f}', 
            ha='right', va='center', fontsize=9)

# Customize the plot
ax.set_ylim(0.2, 1.0)
ax.set_xlim(0.5, 3.5)
ax.set_xticks(x_positions)
ax.set_xticklabels(labels)
ax.set_ylabel('Win Rate Estimate', fontsize=12)
ax.grid(True, alpha=0.3)


plt.tight_layout()
plt.show()