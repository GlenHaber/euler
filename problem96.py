"""
Sudoku

Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit
must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares.
The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row,
column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its
solution grid.

    0 0 3 | 0 2 0 | 6 0 0     4 8 3 | 9 2 1 | 6 5 7
    9 0 0 | 3 0 5 | 0 0 1     9 6 7 | 3 4 5 | 8 2 1
    0 0 1 | 8 0 6 | 4 0 0     2 5 1 | 8 7 6 | 4 9 3
    ------+-------+------     ------+-------+------
    0 0 8 | 1 0 2 | 9 0 0     5 4 8 | 1 3 2 | 9 7 6
    7 0 0 | 0 0 0 | 0 0 8     7 2 9 | 5 6 4 | 1 3 8
    0 0 6 | 7 0 8 | 2 0 0     1 3 6 | 7 9 8 | 2 4 5
    ------+-------+------     ------+-------+------
    0 0 2 | 6 0 9 | 5 0 0     3 7 2 | 6 8 9 | 5 1 4
    8 0 0 | 2 0 3 | 0 0 9     8 1 4 | 2 5 3 | 7 6 9
    0 0 5 | 0 1 0 | 3 0 0     6 9 5 | 4 1 7 | 3 8 2

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to
employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The
complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can
be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles
ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid;
for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""


class Sudoku(object):
    def __init__(self, grid):
        self.grid = grid

    def _row(self, row):
        return self.grid[row]

    def _column(self, col):
        return [self.grid[row][col] for row in range(9)]

    def _box(self, x, y):
        return [[self.grid[3 * x + i][3 * y + j] for j in range(3)] for i in range(3)]

    def _flat_box(self, x, y):
        return [self.grid[3 * x + i][3 * y + j] for i in range(3) for j in range(3)]

    def _fill_options(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    self.grid[i][j] = set(range(1, 10))

    def _limit_options(self, cell=None):
        if cell is None:
            for i in range(9):
                for j in range(9):
                    if isinstance(self.grid[i][j], int):
                        self._limit_options((i, j))
        else:
            # Limit row
            r, c = cell
            value = self.grid[r][c]
            for i in range(0, 9):
                # Limit row
                if i != c and isinstance(self.grid[r][i], set):
                    self.grid[r][i] -= {value}
                # Limit column
                if i != r and isinstance(self.grid[i][c], set):
                    self.grid[i][c] -= {value}
            # Limit smaller square
            x = r // 3
            y = c // 3
            for i in range(3):
                for j in range(3):
                    xi, yj = 3 * x + i, 3 * y + j
                    if isinstance(self.grid[xi][yj], set):
                        self.grid[xi][yj] -= {value}

    def _check_lone_possibilities(self):
        """Check for things like "a 3 can only go in this one place in row X" across the board."""
        changes_made = False
        # Check rows
        for row in range(9):
            options = {v: [] for v in range(1, 10)}
            for col, item in enumerate(self._row(row)):
                if isinstance(item, set):
                    for num in item:
                        options[num].append(col)
            for k, v in options.items():
                if len(v) == 1:
                    self.grid[row][v[0]] = {k}
                    changes_made = True
        # Check columns
        for col in range(9):
            options = {v: [] for v in range(1, 10)}
            for row, item in enumerate(self._column(col)):
                if isinstance(item, set):
                    for num in item:
                        options[num].append(row)
            for k, v in options.items():
                if len(v) == 1:
                    self.grid[v[0]][col] = {k}
                    changes_made = True
        # Check boxes
        for x in range(3):
            for y in range(3):
                box = self._box(x, y)
                options = {v: [] for v in range(1, 10)}
                for i in range(3):
                    for j in range(3):
                        if isinstance(box[i][j], set):
                            for num in box[i][j]:
                                options[num].append((3 * x + i, 3 * y + j))
                for k, v in options.items():
                    if len(v) == 1:
                        self.grid[v[0][0]][v[0][1]] = {k}
                        changes_made = True
        return changes_made


    def _solve_cells(self):
        """Update any solved cells to be ints instead of sets with length 1"""
        updated = set()
        for i in range(9):
            for j in range(9):
                if isinstance(self.grid[i][j], set) and len(self.grid[i][j]) == 1:
                    self.grid[i][j] = self.grid[i][j].pop()
                    updated.add((i, j))
        return updated

    def _completed(self):
        # If there are any sets, it's not completed
        return all(isinstance(self.grid[i][j], int) for i in range(9) for j in range(9))

    def check(self):
        if not self._completed():
            return False
        expected = set(range(1, 10))
        rows = [set(self.grid[i]) for i in range(9)]
        cols = [{self.grid[i][j] for i in range(9)} for j in range(9)]
        boxes = [set(self._flat_box(x, y)) for x in range(3) for y in range(3)]
        return all(x == expected for x in rows + cols + boxes)

    def solve(self):
        self._fill_options()
        self._limit_options()
        while not self._completed():
            updated = self._solve_cells()
            if updated:
                for cell in updated:
                    self._limit_options(cell)
            else:
                updated = self._check_lone_possibilities()
                if not updated:
                    # There isn't enough logic to fully solve some of these.
                    # So I put a breakpoint here and modify self.grid by hand...
                    pass

    def value(self):
        """Get the value used for Project Euler"""
        return int('{}{}{}'.format(*self.grid[0][:3]))

    def print(self):
        for row in self.grid[:3]:
            print('{} {} {} | {} {} {} | {} {} {}'.format(*row))
        print('------+-------+------')
        for row in self.grid[3:6]:
            print('{} {} {} | {} {} {} | {} {} {}'.format(*row))
        print('------+-------+------')
        for row in self.grid[6:]:
            print('{} {} {} | {} {} {} | {} {} {}'.format(*row))


def read_grids(fname):
    grids = []
    with open(fname) as f:
        while True:
            gridname = f.readline()
            if not gridname:
                break
            grids.append([list(map(int, f.readline().strip())) for _ in range(9)])
    return grids


def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def solve_sudoku(puzzle):
    s = Sudoku(puzzle)
    s.solve()
    print(s.value())
    return s.value()


sudokus = read_grids('p096_sudoku.txt')
print(sum(solve_sudoku(sudoku) for sudoku in sudokus))
