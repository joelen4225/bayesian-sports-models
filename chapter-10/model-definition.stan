// Stan Model
data {
    int<lower=0> N; // Total number of games
    int<lower=0> wins; // Number of wins
    real<lower=0> alpha; // Prior alpha
    real<lower=0> beta; // Prior beta
}
parameters {
    real<lower=0, upper=1> theta; // Win rate parameter
}
model {
    theta ~ beta(alpha, beta); // Prior distribution
    wins ~ binomial(N, theta); // Likelihood
}
generated quantities {
    int<lower=0, upper=N> y_rep; // Posterior samples
    y_rep = binomial_rng(N, theta); // Predicted wins
}