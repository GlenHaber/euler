"""
Diophantine equation

Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""
from math import sqrt

from problem64 import continued_fraction


def convergents(n):
    a_parts = continued_fraction(n)

    def a_gen():
        for x in a_parts[0]:
            yield x
        while True:
            for x in a_parts[1]:
                yield x

    a = a_gen()
    a_n2 = next(a)
    a_n1 = next(a)
    h_n2 = a_n2
    h_n1 = a_n2 * a_n1 + 1
    k_n2 = 1
    k_n1 = a_n1
    yield h_n2, k_n2
    yield h_n1, k_n1
    while True:
        a_n = next(a)
        h_n = a_n * h_n1 + h_n2
        k_n = a_n * k_n1 + k_n2
        yield h_n, k_n
        h_n2, h_n1 = h_n1, h_n
        k_n2, k_n1 = k_n1, k_n


def solve_diophantine(D):
    c = convergents(D)
    h, k = 0, 1
    while h ** 2 - D * k ** 2 != 1:
        h, k = next(c)
    return h, k

assert [solve_diophantine(D)[0] for D in (2, 3, 5, 6, 7)] == [3, 2, 9, 5, 8]

if __name__ == '__main__':
    max_D = max_x = 0
    for D in range(1, 1001):
        if sqrt(D).is_integer():
            continue
        h, k = solve_diophantine(D)
        if h > max_x:
            max_D, max_x = D, h
    print('Answer:', max_D)
