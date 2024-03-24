class Calculator:
    def add(self, a, b): # Метод для сложения двух чисел
        result = a + b
        if (a > 0 and b > 0 and result < 0) or (a < 0 and b < 0 and result > 0):
            raise OverflowError("Арифметическое переполнение во время сложения")
        return result

    def subtract(self, a, b): # Метод для вычитания одного числа из другого
        result = a - b
        if (a > 0 and b < 0 and result < 0) or (a < 0 and b > 0 and result > 0):
            raise OverflowError("Арифметическое переполнение во время вычитания")
        return result

    def multiply(self, a, b): # Метод для умножения двух чисел
        result = a * b
        if a != 0 and b != 0 and result / a != b:
            raise OverflowError("Арифметическое переполнение во время умножения")
        return result

    def divide(self, a, b):  # Метод для деления одного числа на другое
        if b == 0:
            raise ValueError("Нельзя делить на ноль")  # Проверка деления на ноль
        return a / b

    def power(self, base, exponent):  # Метод для возведения числа в степень
        if exponent < 0:
            raise ValueError("Показатель степени не может быть отрицательным")  # Проверка отрицательной степени
        return base ** exponent

class Main:
    def main(self) -> None:
        calculator = Calculator()

        print("Сложение: 5 + 3 =", calculator.add(5, 3))
        print("Вычитание: 10 - 7 =", calculator.subtract(10, 7))
        print("Умножение: 7 * 4 =", calculator.multiply(7, 4))
        print("Деление: 12 / 3 =", calculator.divide(12, 3))
        print("Возведение в степень: 2 ^ 3 =", calculator.power(2, 3))


if __name__ == "__main__":
    main = Main()
    main.main()