"""
Поиск максимального числа в списке — тремя способами.
"""


def max_loop(numbers):
    """Способ 1: цикл."""
    max_num = numbers[0]           # Берём первое число как максимум
    for num in numbers:            # Проходим по всем числам
        if num > max_num:          # Если число больше текущего максимума
            max_num = num          # Обновляем максимум
    return max_num


def max_builtin(numbers):
    """Способ 2: встроенная функция max()."""
    return max(numbers)


def max_sorted(numbers):
    """Способ 3: сортировка."""
    return sorted(numbers)[-1]     # Последний элемент — максимальный


if __name__ == "__main__":
    numbers = [1, 4, 15, 7, 8]
    print(max_loop(numbers))
    print(max_builtin(numbers))
    print(max_sorted(numbers))