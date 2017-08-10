# Given two cells on the standard chess board, determine whether they have the same color or not.
#
# Example
# [image missing]
#
# For cell1 = "A1" and cell2 = "C3", the output should be
# chessBoardCellColor(cell1, cell2) = true.
# [image missing]
# 
# For cell1 = "A1" and cell2 = "H3", the output should be
# chessBoardCellColor(cell1, cell2) = false.


def chessBoardCellColor(cell1, cell2):

    first = [x for x in reversed(cell1)]
    first[0] = int(first[0]) - 1
    first[1] = ord(first[1]) - 65

    second = [x for x in reversed(cell2)]
    second[0] = int(second[0]) - 1
    second[1] = ord(second[1]) - 65

    chess_board_reversed = [ [1,0,1,0,1,0,1,0],
                             [0,1,0,1,0,1,0,1],
                             [1,0,1,0,1,0,1,0],
                             [0,1,0,1,0,1,0,1],
                             [1,0,1,0,1,0,1,0],
                             [0,1,0,1,0,1,0,1],
                             [1,0,1,0,1,0,1,0],
                             [0,1,0,1,0,1,0,1] ]

    return chess_board_reversed[first[0]][first[1]] == chess_board_reversed[second[0]][second[1]]
