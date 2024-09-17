import pytest
from statistics import mean, median, mode, standard_deviation

# Набор тестовых данных
test_data = [10, 20, 20, 20, 30, 40, 50]

def test_mean():
    """Тест для проверки функции вычисления среднего арифметического."""
    assert mean(test_data) == 27.142857142857142, "Ошибка в вычислении среднего"

def test_median():
    """Тест для проверки функции вычисления медианы."""
    assert median(test_data) == 20, "Ошибка в вычислении медианы"

def test_mode():
    """Тест для проверки функции вычисления моды."""
    assert mode(test_data) == 20, "Ошибка в вычислении моды"

def test_standard_deviation():
    """Тест для проверки функции вычисления стандартного отклонения."""
    assert pytest.approx(standard_deviation(test_data), 0.001) == 12.1037, "Ошибка в вычислении стандартного отклонения"

# Тесты на проверку обработки исключений
def test_empty_list():
    """Тест для проверки обработки пустого списка."""
    with pytest.raises(ValueError):
        mean([])
    with pytest.raises(ValueError):
        median([])
    with pytest.raises(ValueError):
        mode([])
    with pytest.raises(ValueError):
        standard_deviation([])

def test_mode_with_no_mode():
    """Тест для случая, если нет моды (например, у всех элементов одинаковая частота)."""
    data = [1, 2, 3, 4, 5]
    with pytest.raises(statistics.StatisticsError):
        mode(data)
