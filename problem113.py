"""Non-bouncy numbers

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for
example, 134468. Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for
example, 66420. We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for
example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below
one-million that are not bouncy and only 277032 non-bouncy numbers below 1010.

How many numbers below a googol (10^100) are not bouncy?
"""

# Use a solution similar to the combinatorics method found at http://mathschallenge.net/full/never_decreasing_digits
from common import ncr


def count_increasing(digits):
    return ncr(digits + 9, digits) - 1


def count_decreasing(digits):
    # This is just like count_increasing, but add leading zeros; essentially that means the max value is 10 instead of
    # 9. This will also create multiple copies of 0. The precise number is equal to the number of digits.
    return ncr(digits + 10, digits) - 1 - digits


def count_non_bouncy(digits):
    # There are equally many increasing/decreasing numbers. Double increasing and remove duplicates (i.e., palindromes)
    # Palindromes present are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33,...
    return count_increasing(digits) + count_decreasing(digits) - 9 * digits


def render(pattern):
    val = 0
    number = 0
    for ch in pattern:
        if ch == '0':
            val += 1
        else:
            number = 10 * number + val
    return number


print(count_non_bouncy(100))
