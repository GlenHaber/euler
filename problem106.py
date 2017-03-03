"""
Special subset sums: meta-testing

Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if
for any two non-empty disjoint subsets, B and C, the following properties are true:

    1. S(B) ≠ S(C); that is, sums of subsets cannot be equal.
    2. If B contains more elements than C then S(B) > S(C).

For this problem we shall assume that a given set contains n strictly
increasing elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4,
only 1 of these pairs need to be tested for equality (first rule). Similarly, when n = 7, only 70 out
of the 966 subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?
"""
from itertools import combinations
from math import factorial
from time import time


def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def important_pairs(n):
    """Count the number of n-n pairs that aren't strictly increasing"""
    items = set(range(1, 2 * n))
    important = 0
    for a in combinations(items, n - 1):
        a = (0,) + a
        b = sorted(items - set(a))
        if any(x > y for x, y in zip(a, b)):
            important += 1
    return important


def pairs_to_count(n):
    """Count the number of subset pairs in a group of size n that need to be compared"""
    return sum(ncr(n, 2 * i) * important_pairs(i) for i in range(2, n // 2 + 1))


assert pairs_to_count(4) == 1
assert pairs_to_count(7) == 70
start = time()
print('Answer:', pairs_to_count(12))
print(time() - start)
