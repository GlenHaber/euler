"""
Ordered fractions

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper
fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the
fraction immediately to the left of 3/7.
"""
# Iterate over each d, and find the greatest n for each that is <3/7. Keep track of the greatest n/d while iterating.

def left_of_3_7(max_d):
    floor_n, floor_d = 0, 1
    for d in range(1, max_d + 1):
        val = int(d * 3 / 7)
        if floor_n / floor_d < val / d < 3 / 7:
            floor_n, floor_d = val, d
    return floor_n, floor_d


assert left_of_3_7(8) == (2, 5)
print('{}/{}'.format(*left_of_3_7(1000000)))
