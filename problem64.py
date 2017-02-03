"""
Odd period square roots

All square roots are periodic when written as continued fractions and can be written in the form:

√N = a0 + 1 / (a1 + 1 / (a2 + 1 / (a3 + ... )))

For example, let us consider √23:

√23 = 4 + √23 - 4
    = 4 + 1 / 1 / (√23—4)
    = 4 + 1 / (1 + (√23 – 3)/7)

If we continue we would get the following expansion:

√23 = 4 + 1 / (1 + 1 / (3 + 1 / (1 + 1 / (8 + ...))))

The process can be summarised as follows:

a0 = 4
a1 = 1
a2 = 3
a3 = 1
a4 = 8
a5 = 1
a6 = 3
a7 = 1

It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate
that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
"""
from time import time

from sympy import floor, sqrt
import math


def continued_fraction_sympy(n):
    """Find the coefficients of the continued fraction of sqrt(n)"""
    a = [floor(sqrt(n))]
    remainders = [(1 / (sqrt(n) - a[0])).simplify()]
    while True:
        a.append(floor(remainders[-1]))
        remainder = (1 / (remainders[-1] - a[-1])).simplify()
        if remainder in remainders:
            index = remainders.index(remainder)
            return a[:index + 1], a[index + 1:]
        else:
            remainders.append(remainder)


def continued_fraction(r):
    coeff = [math.floor(math.sqrt(r))]
    pqs = [(math.floor(math.sqrt(r)), 1)]
    while True:
        p, q = pqs[-1]
        qn = (r - p ** 2) // q
        an = math.floor(q / (math.sqrt(r) - p))
        pn = an * qn - p
        coeff.append(an)
        if (pn, qn) in pqs:
            index = pqs.index((pn, qn)) + 1
            return coeff[:index], coeff[index:]
        pqs.append((pn, qn))


def period_length(n):
    return len(continued_fraction(n)[1])

if __name__ == '__main__':
    count = 0
    start = time()
    for i in range(1, 10001):
        if sqrt(i).is_irrational and period_length(i) % 2 == 1:
            count += 1
    print(count)
    print(time()-start)