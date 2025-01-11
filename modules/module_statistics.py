import statistics
import math
from scipy import stats
import random


def mean(data):
    """
    Calculate the mean of a dataset.

    :param data: List of numerical values
    :return: Mean of the dataset
    """
    return statistics.mean(data)


def variance(data):
    """
    Calculate the variance of a dataset.

    :param data: List of numerical values
    :return: Variance of the dataset
    """
    return statistics.variance(data)


def stdev(data):
    """
    Calculate the standard deviation of a dataset.

    :param data: List of numerical values
    :return: Standard deviation of the dataset
    """
    return statistics.stdev(data)


def sample_mean(data):
    """
    Calculate the sample mean of a dataset.

    :param data: List of numerical values
    :return: Sample mean of the dataset
    """
    return statistics.mean(data)


def linear_regression(x, y):
    """
    Perform linear regression on two datasets.

    :param x: List of numerical values (independent variable)
    :param y: List of numerical values (dependent variable)
    :return: Slope and intercept of the regression line
    """
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return slope, intercept


def logarithmic_regression(x, y):
    """
    Perform logarithmic regression on two datasets.

    :param x: List of numerical values (independent variable)
    :param y: List of numerical values (dependent variable)
    :return: Slope and intercept of the regression line
    """
    log_x = [math.log(val) for val in x]
    slope, intercept, r_value, p_value, std_err = stats.linregress(log_x, y)
    return slope, intercept


def z_score(data, value):
    """
    Calculate the z-score of a value in a dataset.

    :param data: List of numerical values
    :param value: Value to calculate the z-score for
    :return: Z-score of the value
    """
    mean = statistics.mean(data)
    stdev = statistics.stdev(data)
    return (value - mean) / stdev


def confidence_interval(data, confidence=0.95):
    """
    Calculate the confidence interval for a dataset.

    :param data: List of numerical values
    :param confidence: Confidence level (default is 0.95)
    :return: Confidence interval
    """
    n = len(data)
    mean = statistics.mean(data)
    stdev = statistics.stdev(data)
    h = stdev * stats.t.ppf((1 + confidence) / 2, n - 1) / math.sqrt(n)
    return mean - h, mean + h


def chi_square(observed, expected):
    """
    Perform a chi-square test.

    :param observed: List of observed frequencies
    :param expected: List of expected frequencies
    :return: Chi-square statistic and p-value
    """
    total_observed = sum(observed)
    total_expected = sum(expected)
    
    if total_observed != total_expected:
        scale_factor = total_observed / total_expected
        expected = [e * scale_factor for e in expected]
    
    try:
        chi2, p = stats.chisquare(observed, expected)
    except ValueError as e:
        raise ValueError(f"Error in chi-square test: {e}")
    return chi2, p


# Example usage
min_items = 5
max_items = 10

data = [random.randint(1, 100) for _ in range(random.randint(min_items, max_items))]
print("Data:", data)
print("Mean:", mean(data))
print("Variance:", variance(data))
print("Standard Deviation:", stdev(data))
print("Sample Mean:", sample_mean(data))
print("Z-Score:", z_score(data, data[0]))
print("Confidence Interval:", confidence_interval(data))

x = [random.randint(1, 100) for _ in range(random.randint(min_items, max_items))]
y = [random.randint(1, 100) for _ in range(len(x))]
print("X:", x)
print("Y:", y)
print("Linear Regression:", linear_regression(x, y))
print("Logarithmic Regression:", logarithmic_regression(x, y))

observed = [random.randint(1, 50) for _ in range(random.randint(min_items, max_items))]
expected = [random.randint(1, 50) for _ in range(len(observed))]
print("Observed:", observed)
print("Expected:", expected)
print("Chi-Square Test:", chi_square(observed, expected))
