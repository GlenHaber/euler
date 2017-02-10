"""
Digit factorial chains

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out
that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting
number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""
from math import factorial
from time import time
MAX_N = 1000000
seqs = [0]*MAX_N


def calc_next(n):
    return sum(factorial(int(x)) for x in str(n))


def chain(n):
    if seqs[n] != 0:
        return seqs[n]
    seq = []
    while n not in seq:
        seq.append(n)
        n = calc_next(n)
    count = len(seq[seq.index(n):])
    for x in seq[-count:]:
        if x < MAX_N:
            seqs[x] = count
    for i, x in enumerate(seq[-count - 1::-1], start=1):
        if x < MAX_N:
            seqs[x] = count + i
    return len(seq)


start = time()
for i in range(MAX_N):
    chain(i)
print(seqs.count(60))
print(time() - start)
