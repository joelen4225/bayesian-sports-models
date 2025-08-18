# Load libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Shape and rate parameters
shapes = [2, 5, 9]  # alpha
rates = [1, 0.65, 0.75]  # beta
n = 100
x = np.linspace(0, 20, n)  # Sequence from 0 to 20

# Create data for plotting
plt.figure(figsize=(10, 6))

# Plot each distribution
for shape, rate in zip(shapes, rates):
    y = gamma.pdf(x, shape, scale=1/rate)
    plt.plot(x, y, linewidth=1.2, label=f'α = {shape}, β = {rate}')

plt.xlabel('X')
plt.ylabel('Density')
plt.title('Gamma Distribution')
plt.legend(title='Distribution')
plt.grid(True, alpha=0.3)
plt.show() 