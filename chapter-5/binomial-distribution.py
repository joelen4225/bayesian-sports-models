# Load libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Number of trials and probabilities of success
n_trials = [10, 20, 30]
probs = [0.45, 0.55, 0.65]
max_x = max(n_trials)

# Create data for plotting
plt.figure(figsize=(10, 6))

# Plot each distribution
for n, p in zip(n_trials, probs):
    x_vals = np.arange(0, n + 1)
    y_vals = binom.pmf(x_vals, n, p)
    plt.plot(x_vals, y_vals, 'o-', linewidth=1.2, markersize=4, 
             label=f'n = {n}, p = {p}')

plt.xlabel('X')
plt.ylabel('Probability')
plt.title('Binomial Distribution')
plt.legend(title='Distribution')
plt.grid(True, alpha=0.3)
plt.show() 