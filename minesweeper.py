# In the popular Minesweeper game you have a board with some mines and
# those cells that don't contain a mine have a number in it that indicates
# the total number of mines in the neighboring cells. Starting off with some
# arrangement of mines we want to create a Minesweeper game setup.
#
# Example
#
# For
#
# matrix = [[true, false, false],
#           [false, true, false],
#           [false, false, false]]
# 
# the output should be
#
# minesweeper(matrix) = [[1, 2, 1],
#                        [2, 1, 1],
#                        [1, 1, 1]]


def minesweeper(matrix):

    temp_list = []
    temp_array = []
    temp_num = 0
    solution = []

    for n in range(len(matrix)):
        for i in range(len(matrix[0])):
            if matrix[n][i] == True:
                temp_list.append(1)
            else:
                temp_list.append(0)
        temp_array.append(temp_list)
        temp_list = []

    for n in range(len(temp_array)):
        for i in range(len(temp_array[0])):
            temp_num = 0
            if n == 0 and i == 0:
                try:
                    temp_num += temp_array[n][i+1]
                except:
                    pass
                try:
                    temp_num += temp_array[n+1][i]
                except:
                    pass
                try:
                    temp_num += temp_array[n+1][i+1]
                except:
                    pass
                temp_list.append(temp_num)
            elif n == 0 and i != 0:
                try:
                    temp_num += temp_array[n][i-1]
                except:
                    pass
                try:
                    temp_num += temp_array[n][i+1]
                except:
                    pass
                try:
                    temp_num += temp_array[n+1][i-1]
                except:
                    pass
                try:
                    temp_num += temp_array[n+1][i]
                except:
                    pass
                try:
                    temp_num += temp_array[n+1][i+1]
                except:
                    pass
                temp_list.append(temp_num)
            elif n != 0 and i == 0:
                try:
                    temp_num += temp_array[n-1][i]
                except:
                    pass
                try:
                    temp_num += temp_array[n-1][i+1]
                except:
                    pass
                try:
                    temp_num += temp_array[n][i+1]
                except:
                    pass
                try:
                    temp_num += temp_array[n+1][i]
                except:
                    pass
                try:
                    temp_num += temp_array[n+1][i+1]
                except:
                    pass
                temp_list.append(temp_num)
            else:
                try:
                    temp_num += temp_array[n-1][i-1]
                except:
                    pass
                try:
                    temp_num += temp_array[n-1][i]
                except:
                    pass
                try:
                    temp_num += temp_array[n-1][i+1]
                except:
                    pass
                try:
                    temp_num += temp_array[n][i-1]
                except:
                    pass
                try:
                    temp_num += temp_array[n][i+1]
                except:
                    pass
                try:
                    temp_num += temp_array[n+1][i-1]
                except:
                    pass
                try:
                    temp_num += temp_array[n+1][i]
                except:
                    pass
                try:
                    temp_num += temp_array[n+1][i+1]
                except:
                    pass
                temp_list.append(temp_num)

        solution.append(temp_list)
        temp_list = []

    return solution
