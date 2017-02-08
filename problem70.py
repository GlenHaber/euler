"""
Totient permutation

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers
less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""
import sys
from itertools import combinations

from problem47 import prime_sieve


def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


assert is_permutation(87109, 79180)
assert not is_permutation(12345, 54320)

# Manually...
# print('This one will take AGES!')
# best = sys.maxsize
# best_n = 0
# for n in range(10**7-1, 2, -1):
#     tot = totient(n)
#     if is_permutation(n, tot) and n/tot < best:
#         best = n/tot
#         best_n = n
# print(best_n)

primes = [p for p in prime_sieve(5000) if p >= 2000]

best_n = 0
best = sys.maxsize
for a, b in combinations(primes, 2):
    n = a * b
    if n >= 10 ** 7:
        continue
    tn = (a - 1) * (b - 1)
    ratio = n / tn
    if is_permutation(n, tn) and ratio < best:
        best = ratio
        best_n = n
print(best_n)
