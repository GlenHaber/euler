"""
Path sum: three ways

In the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column,
and only moving up, down, and right, is 201-96-342-234-103-18 and is equal to 994.

    131 673 234 103  18
    201  96 342 965 150
    630 803 746 422 111
    537 699 497 121 956
    805 732 524  37 331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by
80 matrix, from the left column to the right column.
"""
from copy import deepcopy
from math import inf
from time import time

from problem81 import test_matrix


def find_best_path(matrix):
    scores = deepcopy(matrix)
    scores.append([inf] * len(matrix))  # Avoids needing to handle IndexError
    for column in range(1, len(matrix)):
        for row in range(len(matrix)):
            scores[row][column] += scores[row][column - 1]
        vertical_change = True
        while vertical_change:
            vertical_change = False
            for row in range(len(matrix)):
                adj = min(scores[row - 1][column], scores[row + 1][column])
                if matrix[row][column] + adj < scores[row][column]:
                    scores[row][column] = matrix[row][column] + adj
                    vertical_change = True
    return min(row[-1] for row in scores)


if __name__ == '__main__':
    assert find_best_path(test_matrix) == 994
    start = time()
    with open('p081_matrix.txt') as f:
        bigmat = [list(map(int, line.split(','))) for line in f.read().splitlines()]
    print(find_best_path(bigmat))
    print(time() - start)
