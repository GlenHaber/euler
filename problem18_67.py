"""
Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from
top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                            75
                          95  64
                        17  47  82
                      18  35  87  10
                    20  04  82  47  65
                  19  01  23  75  03  34
                88  02  77  73  07  63  67
              99  65  04  28  06  16  70  92
            41  41  26  56  83  40  80  70  33
          41  48  72  33  47  32  37  16  94  29
        53  71  44  65  25  43  91  52  97  51  14
      70  11  33  28  77  73  17  78  39  68  17  57
    91  71  52  38  17  14  91  43  58  50  27  29  48
  63  66  04  68  89  53  67  30  73  16  69  87  40  31
04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67,
is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)
"""


class Tree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.total = value

    def set_left(self, child):
        self.left = child

    def set_right(self, child):
        self.right = child

    def __str__(self):
        return 'T {}'.format(self.value)

    def __repr__(self):
        s = str(self)
        if self.left or self.right:
            s += ' ({}, {})'.format(self.left, self.right)
        return s


sample = '''3
7 4
2 4 6
8 5 9 3'''
sample_rows = [[Tree(value) for value in map(int, line.split())] for line in sample.splitlines()]


def solve(filename):
    with open(filename) as f:
        rows = [[Tree(value) for value in map(int, line.split())] for line in f]

    for row, next_row in zip(rows[:-1], rows[1:]):
        for i, tree in enumerate(row):
            tree.left = next_row[i]
            tree.right = next_row[i + 1]

    for row in rows[:-1]:
        for tree in row:
            tree.left.total = max(tree.left.total, tree.left.value + tree.total)
            tree.right.total = max(tree.right.total, tree.right.value + tree.total)
    return max(tree.total for tree in rows[-1])

print(solve('18.input'))
print(solve('67.input'))