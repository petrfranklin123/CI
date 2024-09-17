import statistics
import math

def mean(numbers):
    """Функция для вычисления среднего арифметического."""
    if not numbers:
        raise ValueError("Список чисел не может быть пустым.")
    return sum(numbers) / len(numbers)

def median(numbers):
    """Функция для вычисления медианы."""
    if not numbers:
        raise ValueError("Список чисел не может быть пустым.")
    return statistics.median(numbers)

def mode(numbers):
    """Функция для вычисления моды."""
    if not numbers:
        raise ValueError("Список чисел не может быть пустым.")
    return statistics.mode(numbers)

def standard_deviation(numbers):
    """Функция для вычисления стандартного отклонения."""
    if not numbers:
        raise ValueError("Список чисел не может быть пустым.")
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)

if __name__ == "__main__":
    data = [10, 20, 20, 20, 30, 40, 50]
    print(f"Среднее: {mean(data)}")
    print(f"Медиана: {median(data)}")
    print(f"Мода: {mode(data)}")
    print(f"Стандартное отклонение: {standard_deviation(data)}")
