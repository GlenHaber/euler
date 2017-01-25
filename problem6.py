"""
Sum square difference

The sum of the squares of the first ten natural numbers is  1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is   (1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_of_squares(nums):
    return sum(n ** 2 for n in nums)


def square_of_sum(nums):
    return sum(nums) ** 2

def solve(max_number):
    nums = range(1, max_number+1)
    return square_of_sum(nums) - sum_of_squares(nums)

print(solve(10))
print(solve(100))
