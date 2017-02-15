"""
Counting rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

Six 1x1
Four 2x1
Two 3x1
Three 1x2
Two 2x2
One 3x2

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with
the nearest solution.
"""
from itertools import product


def count_rectangles(w, h):
    across = range(1, w + 1)
    down = range(1, h + 1)
    return sum(a * b for a, b in product(across, down))


target = 2000000
x, y = 1, 2
closest = 0
best = x * y
while True:
    count = count_rectangles(x, y)
    if abs(count - target) < abs(closest - target):
        closest = count
        best = x * y
    if count > target:
        if x == y:
            break
        x = y = x + 1
    else:
        y += 1
print(best, '->', closest)
