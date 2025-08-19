# Beta-Binomial updating function
def update_beta(prior_alpha, prior_beta, successes, trials):
    posterior_alpha = prior_alpha + successes
    posterior_beta = prior_beta + (trials - successes)
    return posterior_alpha, posterior_beta

def main():
    # Flat prior parameters
    prior_alpha_flat = 1
    prior_beta_flat = 1
    # Informed prior parameters
    prior_alpha_inf = 4
    prior_beta_inf = 4
    # Observed data
    successes = 6
    trials = 10
    
    # Update the distributions
    posterior_flat = update_beta(prior_alpha_flat, prior_beta_flat, successes, trials)
    posterior_inf = update_beta(prior_alpha_inf, prior_beta_inf, successes, trials)
    print(f"Flat Prior Alpha: {posterior_flat[0]}, Flat Prior Beta: {posterior_flat[1]}")
    print(f"Informed Prior Alpha: {posterior_inf[0]}, Informed Prior Beta: {posterior_inf[1]}")

if __name__ == "__main__":
    main()