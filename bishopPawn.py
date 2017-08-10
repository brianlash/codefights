# Given the positions of a white bishop and a black pawn on the
# standard chess board, determine whether the bishop can capture the pawn in one move.


def bishopAndPawn(bishop, pawn):

    ordinal = abs(ord(bishop[0]) - ord(pawn[0]))

    if (ord(pawn[1]) == ord(bishop[1]) + ordinal) or (ord(pawn[1]) == ord(bishop[1]) - ordinal):
        return True
    else:
        return False
