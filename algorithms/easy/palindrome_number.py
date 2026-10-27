"""
Palindrome Number
https://leetcode.com/problems/palindrome-number/

Дано: целое число x.
Надо: вернуть True, если x — палиндром, иначе False.
"""


def palindrome(x: int) -> bool:
    """Проверяет, является ли число палиндромом."""
    if x < 0:  # Отрицательные не могут быть палиндромами
        return False
    x = str(x)  # Преобразуем число в строку
    return x == x[::-1]  # Сравниваем с перевёрнутой строкой


print(palindrome(121))   # True
print(palindrome(-121))  # False
print(palindrome(10))    # False
print(palindrome(122))   # False
