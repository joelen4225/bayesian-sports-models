# Load libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, beta, binom, gamma, poisson, nbinom

# Set up x ranges for different distributions
x_normal = np.linspace(-4, 4, 100)
x_beta = np.linspace(0, 1, 100)
x_binom = np.arange(0, 21)  # 0:20 in R means 0 to 20 inclusive
x_gamma = np.linspace(0, 10, 100)
x_pois = np.arange(0, 21)  # 0:20 in R means 0 to 20 inclusive
x_nbinom = np.arange(0, 21)  # 0:20 in R means 0 to 20 inclusive

# Parameters for distributions
params = {
    "normal": {"mean": 0, "sd": 1},
    "beta": {"shape1": 2, "shape2": 5},
    "binom": {"size": 20, "prob": 0.5},
    "gamma": {"shape": 2, "scale": 2},
    "poisson": {"lambda": 5},
    "nbinom": {"size": 10, "prob": 0.5}
}

# Define distributions with their functions
distributions = {
    "normal": {
        "pdf": lambda x: norm.pdf(x, loc=params["normal"]["mean"], scale=params["normal"]["sd"]),
        "cdf": lambda x: norm.cdf(x, loc=params["normal"]["mean"], scale=params["normal"]["sd"])
    },
    "beta": {
        "pdf": lambda x: beta.pdf(x, a=params["beta"]["shape1"], b=params["beta"]["shape2"]),
        "cdf": lambda x: beta.cdf(x, a=params["beta"]["shape1"], b=params["beta"]["shape2"])
    },
    "binom": {
        "pmf": lambda x: binom.pmf(x, n=params["binom"]["size"], p=params["binom"]["prob"]),
        "cdf": lambda x: binom.cdf(x, n=params["binom"]["size"], p=params["binom"]["prob"])
    },
    "gamma": {
        "pdf": lambda x: gamma.pdf(x, a=params["gamma"]["shape"], scale=params["gamma"]["scale"]),
        "cdf": lambda x: gamma.cdf(x, a=params["gamma"]["shape"], scale=params["gamma"]["scale"])
    },
    "poisson": {
        "pmf": lambda x: poisson.pmf(x, mu=params["poisson"]["lambda"]),
        "cdf": lambda x: poisson.cdf(x, mu=params["poisson"]["lambda"])
    },
    "nbinom": {
        "pmf": lambda x: nbinom.pmf(x, n=params["nbinom"]["size"], p=params["nbinom"]["prob"]),
        "cdf": lambda x: nbinom.cdf(x, n=params["nbinom"]["size"], p=params["nbinom"]["prob"])
    }
}

# Plot function
def plot_distribution(ax, x, y, title, y_label, is_discrete=False):
    """
    Plots a probability distribution on a given matplotlib axes.
    
    Args:
        ax: matplotlib axes object
        x: x values
        y: y values
        title: plot title
        y_label: y-axis label
        is_discrete: whether the distribution is discrete
    """
    if is_discrete:
        ax.stem(x, y, basefmt=" ", markerfmt="o", linefmt="-")
    else:
        ax.plot(x, y, linewidth=1.2)
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel(y_label)
    ax.grid(True, alpha=0.3)

# Generate probability plots (PMF/PDF)
fig1, axes1 = plt.subplots(2, 3, figsize=(15, 10))
axes1 = axes1.flatten()

# Define the probability plots
probability_plots = [
    (x_normal, distributions["normal"]["pdf"], "Normal PDF", "Density", False),
    (x_beta, distributions["beta"]["pdf"], "Beta PDF", "Density", False),
    (x_binom, distributions["binom"]["pmf"], "Binomial PMF", "Probability", True),
    (x_gamma, distributions["gamma"]["pdf"], "Gamma PDF", "Density", False),
    (x_pois, distributions["poisson"]["pmf"], "Poisson PMF", "Probability", True),
    (x_nbinom, distributions["nbinom"]["pmf"], "Negative Binomial PMF", "Probability", True)
]

# Plot probability functions
for i, (x, func, title, y_label, discrete) in enumerate(probability_plots):
    y = func(x)
    plot_distribution(axes1[i], x, y, title, y_label, discrete)

plt.tight_layout()
plt.show()

# Generate cumulative plots (CDF)
fig2, axes2 = plt.subplots(2, 3, figsize=(15, 10))
axes2 = axes2.flatten()

# Define the cumulative plots
cumulative_plots = [
    (x_normal, distributions["normal"]["cdf"], "Normal CDF", "Probability", False),
    (x_beta, distributions["beta"]["cdf"], "Beta CDF", "Probability", False),
    (x_binom, distributions["binom"]["cdf"], "Binomial CDF", "Probability", True),
    (x_gamma, distributions["gamma"]["cdf"], "Gamma CDF", "Probability", False),
    (x_pois, distributions["poisson"]["cdf"], "Poisson CDF", "Probability", True),
    (x_nbinom, distributions["nbinom"]["cdf"], "Negative Binomial CDF", "Probability", True)
]

# Plot cumulative functions
for i, (x, func, title, y_label, discrete) in enumerate(cumulative_plots):
    y = func(x)
    plot_distribution(axes2[i], x, y, title, y_label, discrete)

plt.tight_layout()
plt.show() 