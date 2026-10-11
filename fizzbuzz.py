"""
FizzBuzz program.

Print numbers from 1 to 100:
- "FizzBuzz" if the number is divisible by both 3 and 5.
- "Fizz" if the number is divisible by 3.
- "Buzz" if the number is divisible by 5.
- Otherwise, print the number itself.
"""


def fizzbuzz(n):
    # Check divisibility by 15 first (both 3 and 5)
    if n % 15 == 0:
        return "FizzBuzz"
    # Check if the number is divisible by 3.
    elif n % 3 == 0:
        return "Fizz"
    # Check if the number is divisible by 5.
    elif n % 5 == 0:
        return "Buzz"
    # If no condition matches, return the number as a string.
    return str(n)


if __name__ == "__main__":
    # Iterate through numbers from 1 to 100 (inclusive).
    for i in range(1, 101):
        # Print the result for each number.
        print(fizzbuzz(i))