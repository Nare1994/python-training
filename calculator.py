"""
Калькулятор: сложение, вычитание, умножение, деление.

Простой калькулятор с четырьмя операциями.
Каждая операция — отдельная функция.
"""


def add(a, b):
    """Сложение: возвращает a + b."""
    return a + b


def subtract(a, b):
    """Вычитание: возвращает a - b."""
    return a - b


def multiply(a, b):
    """Умножение: возвращает a * b."""
    return a * b


def divide(a, b):
    """Деление: возвращает a / b. Если b == 0 — ошибка."""
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


def main():
    """Точка входа: запускает примеры."""
    print(add(2, 3))
    print(subtract(10, 2))
    print(multiply(3, 4))
    print(divide(20, 3))
    print(divide(20, 0))


if __name__ == "__main__":
    main()