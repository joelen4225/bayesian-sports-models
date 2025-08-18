# Load libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Lambda rate parameters
lambdas = [4.5, 6.5, 10]
max_x = 20

# Create data for plotting
plt.figure(figsize=(10, 6))

# Plot each distribution
for lambda_param in lambdas:
    x_vals = np.arange(0, max_x + 1)
    y_vals = poisson.pmf(x_vals, lambda_param)
    plt.plot(x_vals, y_vals, 'o-', linewidth=1.2, markersize=4, 
             label=f'λ = {lambda_param}')

plt.xlabel('X')
plt.ylabel('Probability')
plt.title('Poisson Distribution')
plt.legend(title='Distribution')
plt.grid(True, alpha=0.3)
plt.show() 