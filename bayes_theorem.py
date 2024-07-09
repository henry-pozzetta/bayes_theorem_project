# bayes_theorem.py

class ProbabilityStrategy:
    def calculate_prior(self, data):
        raise NotImplementedError("calculate_prior method not implemented")

    def calculate_likelihood(self, data):
        raise NotImplementedError("calculate_likelihood method not implemented")

    def calculate_marginal(self, data):
        raise NotImplementedError("calculate_marginal method not implemented")

class ExampleProbabilityStrategy(ProbabilityStrategy):
    def calculate_prior(self, data):
        return data['disease_count'] / data['total_population']

    def calculate_likelihood(self, data):
        return data['true_positive_count'] / data['disease_count']

    def calculate_marginal(self, data):
        return data['test_positive_count'] / data['total_population']

def bayes_theorem(data, strategy: ProbabilityStrategy):
    P_A = strategy.calculate_prior(data)
    P_B_given_A = strategy.calculate_likelihood(data)
    P_B = strategy.calculate_marginal(data)
    return (P_B_given_A * P_A) / P_B

# Example usage:
if __name__ == "__main__":
    data = {
        'total_population': 10000,
        'disease_count': 100,
        'test_positive_count': 600,
        'true_positive_count': 99
    }

    strategy = ExampleProbabilityStrategy()
    result = bayes_theorem(data, strategy)
    print("postier probability ", result)  # Output will be the posterior probability

    import numpy as np

    data = np.array([1, 2, 3, 4, 5])
    mean = np.mean(data)
    print("numpy Mean:", mean)

    import pandas as pd

    data = pd.Series([1, 2, 3, 4, 5])
    mean = data.mean()
    print("pandas Mean:", mean)

    from scipy import stats

    data = [1, 2, 3, 4, 5]
    mean = stats.tmean(data)
    print("scipy Mean:", mean)

    import statsmodels.api as sm

    data = sm.datasets.get_rdataset("mtcars").data
    model = sm.OLS(data['mpg'], data[['hp', 'wt']]).fit()
    print("statsmodels Mean", model.summary())

    import matplotlib.pyplot as plt
    import seaborn as sns

    data = [1, 2, 3, 4, 5]
    sns.histplot(data)
    print("matplotlib Mean in popup Window")
    plt.show()


