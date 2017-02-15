"""
Right triangles with integer coordinates

The points P(x1, y1) and Q(x2, y2) are plotted at integer coordinates and are joined to the origin O(0,0) to form OPQ.

There are exactly fourteen triangles containing a right angle that can be formed when each coordinate lies between 0
and 2 inclusive; that is, 0 ≤ x1, y1, x2, y2 ≤ 2.

(0,1), (1,0)    (0,2), (2,0)
(1,0), (1,1)    (0,1), (1,1)
(0,2), (1,0)    (2,0), (0,1)
(1,0), (1,2)    (0,1), (2,1)
(1,1), (2,0)    (1,1), (0,2)
(0,2), (1,2)    (2,0), (2,1)
(0,2), (2,2)    (2,0), (2,2)

Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
"""
import time
from math import gcd


def count_triangles(upper_bound):
    count = upper_bound ** 2
    for x in range(upper_bound + 1):
        for y in range(0 if x else 1, upper_bound + 1):
            dx, dy = y // gcd(x, y), -x // gcd(x, y)
            new_x, new_y = x + dx, y + dy
            while 0 <= new_x <= upper_bound and 0 <= new_y <= upper_bound:
                count += 1
                new_x += dx
                new_y += dy
            new_x, new_y = x - dx, y - dy
            while 0 <= new_x <= upper_bound and 0 <= new_y <= upper_bound:
                count += 1
                new_x -= dx
                new_y -= dy
    return count


if __name__ == '__main__':
    assert count_triangles(2) == 14
    start = time.time()
    print(count_triangles(50))
    print(time.time() - start)
