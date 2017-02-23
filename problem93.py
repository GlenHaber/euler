"""
Arithmetic expressions

By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations
(+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

    8 = (4 * (1 + 3)) / 2
    14 = 4 * (3 + 1 / 2)
    19 = 4 * (2 + 3) − 1
    36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum,
and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n,
can be obtained, giving your answer as a string: abcd.
"""
import operator
from functools import reduce
from itertools import permutations
from math import inf
from time import time


# Copy Operation/Tree classes from my 24 solver
class Operation(object):
    def __init__(self, func, symbol, is_commutative):
        self.func = func
        self.symbol = symbol
        self.is_commutative = is_commutative

    def __call__(self, *args, **kwargs):
        return self.func(args) if self.is_commutative else self.func(*args)

    def __str__(self):
        return self.symbol


add = Operation(lambda *args: sum(*args), '+', True)
sub = Operation(lambda a, b: a - b, '-', False)
mul = Operation(lambda *args: reduce(operator.mul, *args), '*', True)
div = Operation(lambda a, b: (a / b) if b != 0 else inf, '/', False)
all_ops = [add, sub, mul, div]


class Tree(object):
    def __init__(self, op, items):
        self.op = op
        self.items = list(items)
        if not op.is_commutative and len(items) != 2:
            raise ValueError('Non-commutative operation must have two items')

    def evaluate(self):
        items = [i.evaluate() if isinstance(i, Tree) else i for i in self.items]
        result = self.op(*items)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return result


def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def build_trees(items):
    if len(items) == 1:
        return items
    tree_items = []
    for a, b in permutations(items, 2):
        for op in all_ops:
            t = Tree(op, [a, b])
            others = items.copy()
            others.remove(a)
            others.remove(b)
            tree_items.append([t] + others)
    trees = [build_trees(t) for t in tree_items]
    return flatten(trees)


def find_biggest_range(items):
    items = sorted(set(items))
    size = 0
    for i in items:
        if i - size > 1:
            break
        size = i
    return size


def solve(digits):
    values = [t.evaluate() for t in build_trees(digits)]
    values = {v for v in values if isinstance(v, int) and v > 0}
    return find_biggest_range(values)


start = time()
results = [([a, b, c, d], solve([a, b, c, d]))
           for a in range(1, 10) for b in range(a + 1, 10)
           for c in range(b + 1, 10) for d in range(c + 1, 10)]
best = max(results, key=lambda r: r[1])[0]
print('{}{}{}{}'.format(*best))
print(time() - start)
