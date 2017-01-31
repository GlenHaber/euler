"""
Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
from itertools import permutations


def gen_09_pandigitals():
    digits = '0123456789'
    for c in permutations(digits):
        yield int(''.join(c))

def check(num):
    primes = [2, 3, 5, 7, 11, 13, 17]
    sub_numbers = map(int, (str(num)[i:i + 3] for i in range(1, 9)))
    return not any(num % prime for num, prime in zip(sub_numbers, primes))

print(sum(filter(check, gen_09_pandigitals())))