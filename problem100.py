"""
Arranged probability

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken
at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing
eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue
discs that the box would contain.
"""
from math import sqrt

# Find the first solution
blue = 1
total = 1
while True:
    total += 1
    blue = int((2 + sqrt(4 + 8 * (total ** 2 - total))) / 4)
    if 2 * blue * (blue - 1) == total * (total - 1):
        break
# Solving 2x^2-2x-y^2+y=0 at https://www.alpertron.com.ar/QUAD.HTM gives:
# x_n+1 = 3x_n + 2y_n - 2
# y_n+1 = 4x_n + 3y_n - 3
# With x for blue and y for total
while total < 10 ** 12:
    blue, total = 3 * blue + 2 * total - 2, 4 * blue + 3 * total - 3
print(blue)