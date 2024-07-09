Feature: Bayes Theorem Calculation

  Scenario: Calculate posterior probability
    Given a dataset with total population 10000, disease count 100, test positive count 600, and true positive count 99
    When I calculate the posterior probability using Bayes' theorem
    Then the result should be approximately 0.165
