"""
Largest exponential

Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that
2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""
from math import log

with open('p099_base_exp.txt') as f:
    pairs = [tuple(map(int, line.split(','))) for line in f.read().splitlines()]
print(pairs[:3])
best_line = 0
best = 0
for i, nums in enumerate(pairs, start=1):
    base, exp = nums
    log_value = log(base)*exp
    if log_value > best:
        best = log_value
        best_line = i
print(best)
print(best_line)