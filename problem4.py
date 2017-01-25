"""Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import itertools


def is_palindrome(i):
    return str(i) == str(i)[::-1]


def find_large_palindrome(digits):
    mults = range(10 ** (digits - 1), 10 ** digits)
    biggest = 0
    for a, b in itertools.product(mults[::-1], repeat=2):
        if a > b:
            continue
        product = a * b
        if is_palindrome(product) and product > biggest:
            biggest = product
    return biggest


print(find_large_palindrome(2))
print(find_large_palindrome(3))
