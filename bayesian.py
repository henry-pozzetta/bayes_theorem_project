from scipy.integrate import quad
from scipy.stats import binom

def prior(x):
    return 1 if 0 <= x <= 1 else 0

def likelihood(score, x):
    alice_points, bob_points = score
    return binom.pmf(bob_points, alice_points + bob_points, x)

def posterior(score, x):
    return likelihood(score, x) * prior(x)

def calculate_normalization_constant(score):
    normalization_constant, _ = quad(lambda x: posterior(score, x), 0, 1)
    return normalization_constant

def calculate_failure_probability(score):
    normalization_constant = calculate_normalization_constant(score)
    failure_probability, _ = quad(lambda x: posterior(score, x) / normalization_constant, 0, 1)
    return failure_probability

# Example usage for the current score of Alice 5, Bob 3
score = (5, 3)
failure_probability = calculate_failure_probability(score)
print(f"Probability of Bob winning given the current score (Alice 5, Bob 3): {failure_probability:.4f}")
