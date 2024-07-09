Feature: Bayesian Approach to Predicting Game Outcome

  Scenario: Predict probability of Bob winning from score 5-3
    Given the current score is Alice 5, Bob 3
    When we calculate the probability using the Bayesian approach
    Then the probability of Bob winning should be approximately 0.09
