"""
Magic 5-gon ring

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, each line adding to nine.

      4
       \
        3
       / \
      1---2---6
     /
    5

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this
example), each solution can be described uniquely. For example, the above solution can be described by the set:
    4,3,2; 6,2,1; 5,1,3

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9       4,2,3; 5,3,1; 6,1,2
9       4,3,2; 6,2,1; 5,1,3
10      2,3,5; 4,5,1; 6,1,3
10      2,5,3; 6,3,1; 4,1,5
11      1,4,6; 3,6,2; 5,2,4
11      1,6,4; 5,4,2; 3,2,6
12      1,5,6; 2,6,4; 3,4,5
12      1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the
maximum 16-digit string for a "magic" 5-gon ring?
"""
from itertools import permutations


def check_n_ring(order):
    n = len(order) // 2
    spokes = [order[:3]]
    for i in range(1, n - 1):
        spokes.append([order[2 * i + j] for j in (1, 0, 2)])
    spokes.append([order[-1], order[-2], order[1]])
    # Check ordering (smallest spoke first)
    outer = [s[0] for s in spokes]
    if outer[0] != min(outer):
        return 0
    # Check sums
    if len(set(sum(s) for s in spokes)) != 1:
        return 0
    return int(''.join(str(x) for s in spokes for x in s))


best = 0
for p in permutations(range(1, 11)):
    res = check_n_ring(list(p))
    if res < 1e16:
        best = max(best, res)
print(best)
