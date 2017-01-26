"""
Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

RRDD, RDRD, RDDR, DRDR, DDRR

How many such routes are there through a 20×20 grid?
"""
# The solution to this problem is in combinatorics. For an NxN grid, 2N steps need to be taken (N right, N down). A path
# can be considered a sequence of R and D moves, as above. If N of the 2N steps in the path must be D, then there are
# 2N choose N possible paths.
from math import factorial


def count_paths(size):
    # We're only interested in the number of paths, rather than the paths themselves, so just plug in the formula
    return int(factorial(2 * size) / (factorial(size) ** 2))


print(count_paths(2))
print(count_paths(20))
