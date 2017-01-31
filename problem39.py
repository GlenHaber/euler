"""
Integer right triangles

If p is the perimeter of a ring angle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120:
    {20,48,52}
    {24,45,51}
    {30,40,50}

For which value of p <= 1000 is the number of solutions maximized?
"""
import datetime
from math import sqrt
from collections import defaultdict


def count_right_triangles(p):
    count = 0
    for a in range(1, p // 3):
        for b in range(a + 1, (p - a) // 2 + 1):
            if a ** 2 + b ** 2 == (p - a - b) ** 2:
                count += 1
    return count


def alternate():
    counts = defaultdict(lambda: 0)
    for a in range(1, 500):
        for b in range(a + 1, 500):
            c = sqrt(a ** 2 + b ** 2)
            if c.is_integer():
                counts[int(a + b + c)] += 1
    return max(counts.items(), key=lambda item: item[1])[0]


print(count_right_triangles(120))
start = datetime.datetime.now()
print('Answer:', max(range(0, 1000, 2), key=count_right_triangles))
print(datetime.datetime.now() - start)
start = datetime.datetime.now()
print('Answer:', alternate())
print(datetime.datetime.now() - start)
