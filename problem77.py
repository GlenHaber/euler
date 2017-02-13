"""
Prime summations

It is possible to write ten as the sum of primes in exactly five different ways:
7+3
5+5
5+3+2
3+3+2+2
2+2+2+2+2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""
from time import time

from problem47 import prime_sieve

primes = prime_sieve(1000)

# Fast method; if there are x ways to create j-i, then there are sum(x) over i ways to create j.
start = time()
ways = [0] * 101
ways[0] = 1
for i in range(100):
    for j in range(primes[i], 101):
        ways[j] += ways[j - primes[i]]
big = [w for w in ways if w > 5000]
print(ways.index(big[0]))
print(time() - start)

start = time()
values = [0] * primes[-1] * 5

# Brute force with a sum of at least 5 primes
for ai, a in enumerate(primes):
    for bi, b in enumerate(primes[ai:], start=ai):
        values[a + b] += 1
        for ci, c in enumerate(primes[bi:], start=bi):
            values[a + b + c] += 1
            for di, d in enumerate(primes[ci:], start=ci):
                values[a + b + c + d] += 1
                for ei, e in enumerate(primes[di:], start=di):
                    values[a + b + c + d + e] += 1
for i, v in enumerate(values):
    if v >= 5000:
        print(i)
        break
print(time() - start)
