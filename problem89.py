"""
Roman numerals

For a number written in Roman nrumerals to be considered valid there are basic rules which must be followed. Even though
the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular
number.

For example, it would appear that there are at least six ways of writing the number sixteen:

    IIIIIIIIIIIIIIII
    VIIIIIIIIIII
    VVIIIIII
    XIIIIII
    VVVI
    XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most
efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid,
but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.
"""
from math import log10
from time import time

ra_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
ar_values = {v: k for k, v in ra_values.items()}


def roman_to_arabic(roman):
    chars = [ra_values[ch] for ch in roman]
    total = 0
    last_ch = 0
    for ch in chars[::-1]:
        if ch >= last_ch:
            total += ch
        else:
            total -= ch
        last_ch = ch
    return total


sixteens = ['IIIIIIIIIIIIIIII', 'VIIIIIIIIIII', 'VVIIIIII', 'XIIIIII', 'VVVI', 'XVI']
assert all(roman_to_arabic(x) == 16 for x in sixteens)


def arabic_to_roman(num):
    roman = ''
    while num > 0:
        if num > max(ar_values):
            roman += ar_values[max(ar_values)]
            num -= max(ar_values)
            continue
        first_digit = num // 10 ** int(log10(num))
        mag = 10 ** int(log10(num))
        if first_digit in (4, 9):
            num += mag
            roman += ar_values[mag]
        elif first_digit >= 5:
            num -= 5 * mag
            roman += ar_values[5 * mag]
        else:
            num -= first_digit * mag
            roman += ar_values[mag] * first_digit
    return roman


assert arabic_to_roman(43) == 'XLIII'
assert arabic_to_roman(1986) == 'MCMLXXXVI'
assert arabic_to_roman(49) == 'XLIX'

start = time()
nums = [n.strip() for n in open('p089_roman.txt')]
print(sum(len(n) - len(arabic_to_roman(roman_to_arabic(n))) for n in nums))
print(time() - start)
