"""
Double-base palindromes

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


def check(n):
    d = str(n)
    b = bin(n)[2:]
    return d == d[::-1] and b == b[::-1]


print(sum(filter(check, range(1, 1000000))))
