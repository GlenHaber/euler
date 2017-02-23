"""
Almost equilateral triangles

It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the
almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by
no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose
perimeters do not exceed one billion (1,000,000,000).
"""
# Triangle a,a,b has area hb/2, with a^2=h^2+(b/2)^2. This can be turned into Pell's equation, x^2 - Dy^2 = 1
# For b = a+1:
#         a^2 = h^2 + ((a+1)/2)^2 = h^2 + (a+1)^2/4
#        4a^2 = 4h^2 + (a+1)^2 = 4h^2 + a^2 + 2a + 1
#        4h^2 = 3a^2 - 2a - 1
#       12h^2 = 9a^2 - 6a - 3
#   12h^2 + 4 = 9a^2 - 6a + 1 = (3a-1)^2
#           4 = (3a-1)^2 - 12h^2
#           1 = ((3a-1)/2)^2 - 3h^2
# Which is Pell's equation with x=(3a-1)/2, y=h, and n=3
# For b = a-1, x=(3a+1)/2.
from time import time

from problem66 import solve_diophantine


def solutions(n):
    x1, y1 = solve_diophantine(n)
    yield x1, y1
    xk, yk = x1, y1
    while True:
        xk, yk = x1 * xk + n * y1 * yk, x1 * yk + y1 * xk
        yield xk, yk


start = time()
# Get base solution with continued fraction
sols = solutions(3)
total = 0
a1x3, a2x3 = 0, 0
CEILING = 1000000000
while True:
    x, y = next(sols)
    # x = (3a+-1)/2 ==> a = (2x+-1)/3
    a1x3 = (2 * x + 1)
    A1x3 = y * (x + 2)
    a2x3 = (2 * x - 1)
    A2x3 = y * (x - 2)
    if a2x3 > CEILING:
        break
    if a1x3 % 3 == 0 and A1x3 % 3 == 0 and A1x3:
        total += a1x3 + 1
    if a2x3 % 3 == 0 and A2x3 % 3 == 0 and A2x3:
        total += a2x3 - 1

print(total)
print(time() - start)

"""The solution below just didn't work. Need to investigate why."""
# from problem61 import is_square
#
#
# def gen_squares(ceiling):
#     x = 0
#     while True:
#         x += 1
#         yield x ** 2
#         if x ** 2 > ceiling:
#             break
#
# CEILING = 1000000000
# # squares = {x**2 for x in range(1, 577350270)}
# # print(len(squares), max(squares))
#
#
# def has_integral_area(x, y):
#     """
#     See if a triangle with sides x, x, y has integral area.
#
#     Given side lengths (a,b,c), a triangle has area sqrt( s(s-a)(s-b)(s-c) ), where s = (a+b+c)/2.
#     This means that the triangle has integral area if s(s-a)(s-b)(s-c) is a perfect square. For sides (x,x,y), this
#     becomes s(s-x)(s-x)(x-y). (s-x) is a repeated factor, so we can just check to see if s(s-y) is a perfect square.
#     """
#     if x+x+y > CEILING or x+x+y < 3:
#         return False
#     s = (x + x + y) / 2
#     return is_square(s * (s - y))
#
#
# assert has_integral_area(5, 6)
#
# start = time()
# total = 0
# print(sum(x + x + y for x in range(1, CEILING // 3 + 5) for y in (x + 1, x - 1) if has_integral_area(x, y)))
# print(time() - start)
