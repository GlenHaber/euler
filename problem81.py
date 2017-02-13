"""
Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and
down, is 131-201-96-342-746-422-121-37-331 and is equal to 2427.

    131 673 234 103  18
    201  96 342 965 150
    630 803 746 422 111
    537 699 497 121 956
    805 732 524  37 331

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by
80 matrix, from the top left to the bottom right by only moving right and down.
"""

test_matrix = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]


def find_best_path(matrix):
    sz = 2 * (len(matrix) - 1)  # Total steps to take
    for i in range(1, sz + 1):
        r = 0
        c = i
        while c >= len(matrix):
            r += 1
            c -= 1
        while c >= 0 and r < len(matrix):
            if r == 0:
                matrix[r][c] += matrix[r][c - 1]
            elif c == 0:
                matrix[r][c] += matrix[r - 1][c]
            else:
                matrix[r][c] += min(matrix[r][c - 1], matrix[r - 1][c])
            r += 1
            c -= 1
    return matrix[-1][-1]

if __name__ == '__main__':
    assert find_best_path(test_matrix) == 2427
    with open('p081_matrix.txt') as f:
        bigmat = [list(map(int, line.split(','))) for line in f.read().splitlines()]
    print(find_best_path(bigmat))
