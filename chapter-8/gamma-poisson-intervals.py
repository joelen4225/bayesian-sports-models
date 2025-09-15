import numpy as np
import matplotlib.pyplot as plt

# Gamma-Poisson Model Example
# Observed goals in a series of games
observed_goals = [3, 5, 2, 1, 6, 4, 3]
sum_goals = sum(observed_goals)
n_games = len(observed_goals)

# Simulate Gamma (30, 9) posterior distribution
shape = 30
rate = 9
n_sim = 10000
lambda_sim = np.random.gamma(shape, 1/rate, n_sim)

# Calculate 95% credible interval for lambda
credible_interval_gamma = np.percentile(lambda_sim, [2.5, 97.5])
mean_credible_gamma = np.mean(lambda_sim)

# Calculate MLE and standard error for lambda 
lambda_mle = sum_goals / n_games
se_lambda = np.sqrt(lambda_mle / n_games)
conf_interval_gamma = [lambda_mle - 1.96 * se_lambda, lambda_mle + 1.96 * se_lambda]
mean_conf_gamma = lambda_mle

# Create the plot
fig, ax = plt.subplots(figsize=(6, 8))

# Plot the two intervals
x_positions = [2, 1]  # Bayesian at top, Frequentist at bottom
intervals = [credible_interval_gamma, conf_interval_gamma]
labels = ['Bayesian Credible Interval', 'Frequentist Confidence Interval']

for i, (interval, label) in enumerate(zip(intervals, labels)):
    # Plot the interval as a vertical black line
    ax.plot([x_positions[i], x_positions[i]], interval, color='black', linewidth=3)
    
    # Plot the min as a blue dot
    ax.plot(x_positions[i], interval[0], 'o', color='blue', markersize=8)
    
    # Plot the max as a red dot
    ax.plot(x_positions[i], interval[1], 'o', color='red', markersize=8)
    
    # Add text labels for the interval bounds
    ax.text(x_positions[i] - 0.1, interval[0], f'{interval[0]:.2f}', 
            ha='right', va='center', fontsize=9)
    ax.text(x_positions[i] - 0.1, interval[1], f'{interval[1]:.2f}', 
            ha='right', va='center', fontsize=9)

# Customize the plot
ax.set_ylim(0, max(max(credible_interval_gamma), max(conf_interval_gamma)) + 0.5)
ax.set_xlim(0.5, 2.5)
ax.set_xticks(x_positions)
ax.set_xticklabels(labels)
ax.set_ylabel('Goal Scoring Range', fontsize=12)
ax.set_xlabel('Method', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

