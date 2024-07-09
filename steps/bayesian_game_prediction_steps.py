from behave import given, when, then
from bayesian import calculate_failure_probability

@given('the current score is Alice 5, Bob 3')
def step_given_current_score(context):
    context.score = (5, 3)

@when('we calculate the probability using the Bayesian approach')
def step_when_calculate_bayesian_probability(context):
    context.bayesian_probability = calculate_failure_probability(context.score)

@then('the probability of Bob winning should be approximately 0.09')
def step_then_check_probability(context):
    assert abs(context.bayesian_probability - 0.09) < 0.01, f"Expected approximately 0.09, but got {context.bayesian_probability}"
