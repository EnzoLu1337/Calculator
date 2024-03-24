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

def test_power_positive_exponent(calculator):
    # Проверка возведения числа в положительную степень
    assert calculator.power(2, 3) == 8

def test_power_negative_exponent(calculator):
    # Проверка возведения числа в отрицательную степень
    assert calculator.power(2, -3) == 0.125

def test_power_zero_base(calculator):
    # Проверка возведения нуля в любую степень (должен быть равен нулю)
    assert calculator.power(0, 5) == 0

def test_power_zero_exponent(calculator):
    # Проверка возведения числа в нулевую степень (должен быть равен 1)
    assert calculator.power(5, 0) == 1

def test_power_negative_base(calculator):
    # Проверка возведения отрицательного числа в степень
    assert calculator.power(-2, 3) == -8

def test_power_even_exponent_of_negative_base(calculator):
    # Проверка возведения отрицательного числа в четную степень
    assert calculator.power(-2, 2) == 4

def test_power_odd_exponent_of_negative_base(calculator):
    # Проверка возведения отрицательного числа в нечетную степень
    assert calculator.power(-2, 3) == -8