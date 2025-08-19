# Gamma-Poisson updating function
def update_gamma(prior_alpha, prior_beta, observed_sum, n):
    posterior_alpha = prior_alpha + observed_sum
    posterior_beta = prior_beta + n
    return posterior_alpha, posterior_beta

def main():
    # Flat prior parameters
    prior_alpha_flat = 1
    prior_beta_flat = 1
    # Informed prior parameters
    prior_alpha_inf = 6
    prior_beta_inf = 2
    # Observed data
    observed_goals = [3, 5, 2, 1, 6, 4, 3]
    sum_goals = sum(observed_goals)
    n = len(observed_goals)
    # Update the distributions
    posterior_flat = update_gamma(prior_alpha_flat, prior_beta_flat, sum_goals, n)
    posterior_inf = update_gamma(prior_alpha_inf, prior_beta_inf, sum_goals, n)
    print(f"Flat Prior Alpha: {posterior_flat[0]}, Flat Prior Beta: {posterior_flat[1]}")
    print(f"Informed Prior Alpha: {posterior_inf[0]}, Informed Prior Beta: {posterior_inf[1]}")

if __name__ == "__main__":
    main()