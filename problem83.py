"""
Path sum: four ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and
down, is 131-201-96-342-234-103-18-150-111-422-121-37-331 and is equal to 2297.

    131 673 234 103  18
    201  96 342 965 150
    630 803 746 422 111
    537 699 497 121 956
    805 732 524  37 331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by
80 matrix, from the top left to the bottom right by moving left, right, up, and down.
"""

from math import inf
from time import time

from problem81 import test_matrix


def a_star(matrix):
    scores = [[inf for _ in range(len(matrix))] for _ in range(len(matrix))]
    scores[0][0] = matrix[0][0]
    last_added = {(0, 0)}
    while last_added:
        cells = last_added
        last_added = set()
        for r, c in cells:
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if not (0 <= r + dr < len(matrix) and 0 <= c + dc < len(matrix)):
                    continue
                old_value = scores[r + dr][c + dc]  # Score already in that cell
                new_value = scores[r][c] + matrix[r + dr][c + dc]  # Score if we come from r,c instead
                if new_value < old_value:
                    scores[r + dr][c + dc] = new_value
                    last_added.add((r + dr, c + dc))
    return scores[-1][-1]


if __name__ == '__main__':
    assert a_star(test_matrix) == 2297
    start = time()
    with open('p081_matrix.txt') as f:
        bigmat = [list(map(int, line.split(','))) for line in f.read().splitlines()]
    print(a_star(bigmat))
    print(time() - start)

