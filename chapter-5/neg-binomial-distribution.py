# Load libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nbinom

# Mean and dispersion parameters
means = [10, 10, 10]
dispersions = [12, 22, 42]
max_x = 35

# Calculate negative binomial parameters (size and prob)
sizes = [(mean**2) / (dispersion - mean) for mean, dispersion in zip(means, dispersions)]
probs = [mean / dispersion for mean, dispersion in zip(means, dispersions)]

# Create data for plotting
plt.figure(figsize=(10, 6))

# Plot each distribution
for mean, dispersion, size, prob in zip(means, dispersions, sizes, probs):
    x_vals = np.arange(0, max_x + 1)
    y_vals = nbinom.pmf(x_vals, size, prob)
    plt.plot(x_vals, y_vals, 'o-', linewidth=1.2, markersize=4, 
             label=f'μ = {mean}, θ = {dispersion}')

plt.xlabel('X')
plt.ylabel('Probability')
plt.title('Negative Binomial Distribution')
plt.legend(title='Distribution')
plt.grid(True, alpha=0.3)
plt.show() 