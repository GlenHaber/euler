"""
Cubic permutations

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact,
41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""
from collections import defaultdict
from time import time

# Method one
start = time()
cubes = {n ** 3: ''.join(sorted(str(n ** 3))) for n in
         range(22, 10000)}  # Start at 22 because 22^3 is the first with 5 digits
cube_digits = {digits: [c for c in cubes if cubes[c] == digits] for digits in set(cubes.values())}
five = {k: v for k, v in cube_digits.items() if len(v) == 5}
print(min([min(x) for x in five.values()]))
print(time() - start)

# Method two -table with counts is MUCH faster
start = time()
counts = defaultdict(lambda: 0)
for n in range(22, 10000):
    counts[''.join(sorted(str(n ** 3)))] += 1
digits = min(k for k, v in counts.items() if v == 5)
for i in range(22, 10000):
    if ''.join(sorted(str(i ** 3))) == digits:
        print(i ** 3)
        break
print(time() - start)
