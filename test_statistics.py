import pytest
from my_statistics import mean, median, mode, standard_deviation
# import statistics as stats

test_data = [10, 20, 20, 20, 30, 40, 50]

def test_mean():
    assert mean(test_data) == 27.142857142857142

def test_median():
    assert median(test_data) == 20

def test_mode():
    assert mode(test_data) == 20

def test_standard_deviation():
    assert pytest.approx(standard_deviation(test_data), 0.0001) == 12.777531299998799

def test_empty_list():
    with pytest.raises(ValueError):
        mean([])
    with pytest.raises(ValueError):
        median([])
    with pytest.raises(ValueError):
        mode([])
    with pytest.raises(ValueError):
        standard_deviation([])

# def test_mode_no_unique_mode():
#     data = [1, 2, 3, 4, 5]
#     with pytest.raises(stats.StatisticsError):
#         mode(data)
