# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid
# with digits so that each column, each row, and each of the nine 3 × 3
# sub-grids that compose the grid contains all of the digits from 1 to 9.
#
# This algorithm should check if the given grid of numbers
# represents a correct solution to Sudoku.


def sudoku(grid):

    valid_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    # check horizontals
    for x in range(9):
        if set(grid[x]) != valid_set:
            return False

    # check verticals
    for x in range(9):
        if set(list(zip(*grid))[x]) != valid_set:
            return False

    # check 3x3 sub-grids
    # first column of sub-grids...
    temp = []
    for x in range(3):
        for y in range(3):
            temp.append(grid[x][y])
    if set(temp) != valid_set:
        return False
    temp = []
    for x in range(3,6):
        for y in range(3):
            temp.append(grid[x][y])
    if set(temp) != valid_set:
        return False
    temp = []
    for x in range(6,9):
        for y in range(3):
            temp.append(grid[x][y])
    if set(temp) != valid_set:
        return False

    # second column of sub-grids...
    temp = []
    for x in range(3):
        for y in range(3,6):
            temp.append(grid[x][y])
    if set(temp) != valid_set:
        return False
    temp = []
    for x in range(3,6):
        for y in range(3,6):
            temp.append(grid[x][y])
    if set(temp) != valid_set:
        return False
    temp = []
    for x in range(6,9):
        for y in range(3,6):
            temp.append(grid[x][y])
    if set(temp) != valid_set:
        return False

    # third column of sub-grids...
    temp = []
    for x in range(3):
        for y in range(6,9):
            temp.append(grid[x][y])
    if set(temp) != valid_set:
        return False
    temp = []
    for x in range(3,6):
        for y in range(6,9):
            temp.append(grid[x][y])
    if set(temp) != valid_set:
        return False
    temp = []
    for x in range(6,9):
        for y in range(6,9):
            temp.append(grid[x][y])
    if set(temp) != valid_set:
        return False

    return True
