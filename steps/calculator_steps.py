from behave import given, when, then
import bayes_theorem
import math

@given('a dataset with total population {total_population:d}, disease count {disease_count:d}, test positive count {test_positive_count:d}, and true positive count {true_positive_count:d}')
def step_given_dataset(context, total_population, disease_count, test_positive_count, true_positive_count):
    context.data = {
        'total_population': total_population,
        'disease_count': disease_count,
        'test_positive_count': test_positive_count,
        'true_positive_count': true_positive_count
    }

@when("I calculate the posterior probability using Bayes' theorem")
def step_when_calculate_posterior(context):
    strategy = bayes_theorem.ExampleProbabilityStrategy()
    context.result = bayes_theorem.bayes_theorem(context.data, strategy)

@then('the result should be approximately {expected_result:f}')
def step_then_verify_result(context, expected_result):
    assert math.isclose(context.result, expected_result, rel_tol=1e-2), f"Expected {expected_result}, but got {context.result}"
