import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

# Тест проверяет корректность сложения положительных чисел
def test_add_positive_numbers(calculator):
    assert calculator.add(2, 3) == 5

# Тест проверяет корректность сложения отрицательных чисел
def test_add_negative_numbers(calculator):
    assert calculator.add(-2, -3) == -5

# Тест проверяет корректность вычитания положительных чисел
def test_subtract_positive_numbers(calculator):
    assert calculator.subtract(5, 3) == 2

# Тест проверяет корректность вычитания отрицательных чисел
def test_subtract_negative_numbers(calculator):
    assert calculator.subtract(-5, -3) == -2

# Тест проверяет корректность умножения положительных чисел
def test_multiply_positive_numbers(calculator):
    assert calculator.multiply(2, 3) == 6

# Тест проверяет корректность умножения отрицательных чисел
def test_multiply_negative_numbers(calculator):
    assert calculator.multiply(-2, -3) == 6

# Тест проверяет корректность деления положительных чисел
def test_divide_positive_numbers(calculator):
    assert calculator.divide(6, 3) == 2

# Тест проверяет корректность деления отрицательных чисел
def test_divide_negative_numbers(calculator):
    assert calculator.divide(-6, -3) == 2

# Тест проверяет деление на ноль
def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(6, 0)