# Construct a square matrix with a size N × N containing integers from
# 1 to N * N in a spiral order, starting from top-left
# and in clockwise direction.

# Example

# For n = 3, the output should be

# spiralNumbers(n) = [[1, 2, 3],
#                    [8, 9, 4],
#                    [7, 6, 5]]


def spiralNumbers(n):

    matrix = []
    to_allocate = n ** 2
    allocate_next = 1

    # initialize the matrix with placeholders
    for x in range(n):
        temp = []
        for y in range(n):
            temp.append('x')
        matrix.append(temp)

    # define the number of steps the "walk" needs to take at each turn
    partial_path = []

    for x in range(1,n):
        partial_path.append(x)
        partial_path.append(x)

    full_path = [x for x in reversed(partial_path)]

    # do the first row:
    for x in range(len(matrix[0])):
        matrix[0][x] = allocate_next
        allocate_next += 1

    current_x = 0
    current_y = len(matrix[0]) - 1

    while True:
        # down
        if allocate_next <= to_allocate:
            for x in range(current_x + 1, current_x + full_path[0] + 1):
                matrix[x][current_y] = allocate_next
                allocate_next += 1
                current_x += 1
            del full_path[0]
        else:
            break
        # left
        if allocate_next <= to_allocate:
            for y in reversed(range(current_y - full_path[0], current_y)):
                matrix[current_x][y] = allocate_next
                allocate_next += 1
                current_y -= 1
            del full_path[0]
        else:
            break
        # up
        if allocate_next <= to_allocate:
            for x in reversed(range(current_x - full_path[0], current_x)):
                matrix[x][current_y] = allocate_next
                allocate_next += 1
                current_x -= 1
            del full_path[0]
        else:
            break
        # right
        if allocate_next <= to_allocate:
            for y in range(current_y + 1, current_y + full_path[0] + 1):
                matrix[current_x][y] = allocate_next
                allocate_next += 1
                current_y += 1
            del full_path[0]
        else:
            break

    return matrix
