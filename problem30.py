"""
Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
import math


def digit_power_sum(num, power):
    return sum(int(x) ** power for x in str(num))


def ceiling(power):
    i = power
    while math.ceil(math.log10(i * 9 ** power)) >= i:
        i += 1
    return 10 ** i - 1


def total_digit_power_sum(power):
    return sum(n for n in range(10, ceiling(power)) if digit_power_sum(n, power) == n)


print(total_digit_power_sum(4))
print(total_digit_power_sum(5))
