"""
Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

The square of the sum of the first ten natural numbers is
(1 + 2 + ... + 10)² = 55² = 3025.

The sum of the squares of the first ten natural numbers is
1² + 2² + ... + 10² = 385.

Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares 
of the first ten natural numbers is 3025 - 385 = 2640.
"""


def square_of_sum(number):
    numbers = range(1, number + 1)
    square_of_sum = sum(numbers) ** 2
    return square_of_sum


def sum_of_squares(number):
    numbers = range(1, number + 1)
    sum_of_squares = sum(i**2 for i in numbers)
    return sum_of_squares


def difference_of_squares(number):
    difference_of_squares = square_of_sum(number) - sum_of_squares(number)
    return difference_of_squares
