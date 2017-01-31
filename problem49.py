"""
Prime permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
 - Each of the three terms are prime
 - Each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting
this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from collections import defaultdict

from problem47 import prime_sieve

primes = [p for p in prime_sieve(10000) if p > 1000]
primes_by_digits = defaultdict(list)
for p in primes:
    primes_by_digits[''.join(sorted(str(p)))].append(p)
candidates = [v for k, v in primes_by_digits.items() if len(v) >= 3]


def check(seq):
    for p in seq:
        if p + 3330 in seq and p + 6660 in seq:
            print('{}{}{}'.format(p, p + 3330, p + 6660))
            return


for c in candidates:
    check(c)
