# Given a position of a knight on the standard chessboard,
# find the number of different moves the knight can perform.

# The knight can move to a square that is two squares horizontally
# and one square vertically, or two squares vertically and one square
# horizontally away from it. The complete move therefore looks
# like the letter L. Check out the image below to see all valid moves
# for a knight piece that is placed on one of the central squares.


def chessKnight(cell):

    first = ord(cell[0]) - 96
    second = int(cell[1])
    valid = 0

    coords = {}

    coords['first'] = [first + 2, second + 1]
    coords['second'] = [first + 2, second - 1]
    coords['third'] = [first + 1, second + 2]
    coords['fourth'] = [first + 1, second - 2]
    coords['fifth'] = [first - 1, second + 2]
    coords['sixth'] = [first - 1, second - 2]
    coords['seventh'] = [first - 2, second + 1]
    coords['eighth'] = [first - 2, second - 1]

    for x in coords:
        if 1 <= coords[x][0] <= 8 and 1 <= coords[x][1] <= 8:
            valid += 1

    return valid
