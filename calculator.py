"""
Calculator: addition, subtraction, multiplication, and division.

A simple calculator with four operations.
Each operation is implemented as a separate function.
"""


def add(a, b):
    """Addition: returns a + b."""
    return a + b


def subtract(a, b):
    """Subtraction: returns a - b."""
    return a - b


def multiply(a, b):
    """Multiplication: returns a * b."""
    return a * b


def divide(a, b):
    """Division: returns a / b. Returns an error if b == 0."""
    if b == 0:
        return "Error: division by zero"
    return a / b


def main():
    """Entry point: runs example calculations."""
    print(add(2, 3))
    print(subtract(10, 2))
    print(multiply(3, 4))
    print(divide(20, 3))


if __name__ == "__main__":
    main()