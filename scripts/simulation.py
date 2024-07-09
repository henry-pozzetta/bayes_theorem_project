import numpy as np

def simulate_games(num_simulations=10000):
    wins = 0
    for _ in range(num_simulations):
        alice_score, bob_score = 5, 3
        while alice_score < 6 and bob_score < 6:
            if np.random.rand() < 0.375:
                bob_score += 1
            else:
                alice_score += 1
        if bob_score == 6:
            wins += 1
    return wins / num_simulations

if __name__ == "__main__":
    probability_bob_wins = simulate_games()
    print(f"Simulated probability of Bob winning: {probability_bob_wins}")
