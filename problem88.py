"""
Product-sum numbers

A natural number N that can be written as the sum and product of a given set of at least two natural numbers,
{a1, a2, ... , ak} is called a product sum number: N = a1+a2+...+ak = a1*a2*...*ak.

For example, 6 = 1 + 2 + 3 = 1 * 2 * 3

For a given set of size k, we shall call the smallest N with this property a minimal product-sum number. The minimal
product-sum numbers for sets of size k=2, 3, 4, 5 and 6 are as follows:

    k=2: 4 = 2*2 = 2+2
    k=3: 6 = 1*2*3 = 1+2+3
    k=4: 8 = 1*1*2*4 = 1+1+2+4
    k=5: 8 = 1*1*2*2*2 = 1+1+2+2+2
    k=6: 12 = 1*1*1*1*2*6 = 1+1+1+1+2+6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in
the sum. In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
"""
from math import log
from functools import reduce
from itertools import combinations_with_replacement
from operator import mul
from time import time


def combos(digits, max_product):
    nums = [2] * digits
    d = 0
    while True:
        yield nums[::-1]
        nums[d] += 1
        while reduce(mul, nums) > max_product:
            if len(set(nums)) == 1:
                return
            d += 1
            nums[d] += 1
            nums[:d] = [nums[d]] * d
        d = 0


def solve2(max_k):
    best = {n: 2 * n for n in range(2, max_k + 1)}
    max_digits = int(log(max_k, 2) + 1)
    for digits in range(2, max_digits + 1):
        for combo in combos(digits, 2 * max_k):
            product = reduce(mul, combo)
            sum_ = sum(combo)
            ones = product - sum_
            if digits + ones > max_k:
                continue
            best[digits + ones] = min(best[digits + ones], product)
    return sum(set(best.values()))


assert solve2(12) == 61
start = time()
print(solve2(12000))
print(time() - start)
