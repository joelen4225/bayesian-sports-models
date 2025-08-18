# Load libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Define parameters
alphas = [1, 2, 5]  # shape1
betas = [1, 2, 5]   # shape2
n = 100
x = np.linspace(0, 1, n)  # Sequence from 0 to 1

# Create data for plotting
plt.figure(figsize=(10, 6))

# Plot each distribution
for alpha, beta_param in zip(alphas, betas):
    y = beta.pdf(x, alpha, beta_param)
    plt.plot(x, y, linewidth=1.2, label=f'α = {alpha}, β = {beta_param}')

plt.xlabel('X')
plt.ylabel('Density')
plt.title('Beta Distribution')
plt.legend(title='Distribution')
plt.grid(True, alpha=0.3)
plt.show() 