# Load libraries
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
means = [-2, 0, 2]  # mu
sds = [0.5, 1, 1.5]  # sigma
n = 100
x = np.linspace(-10, 10, n)  # Sequence of values

# Create data for plotting
plt.figure(figsize=(10, 6))

# Plot each distribution
for i, (mean, sd) in enumerate(zip(means, sds)):
    y = (1 / (sd * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / sd) ** 2)
    plt.plot(x, y, linewidth=1.2, label=f'μ = {mean}, σ = {sd}')

plt.xlabel('X')
plt.ylabel('Density')
plt.title('Normal Distribution')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
