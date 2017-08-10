# Last night you had to study, but decided to party instead. Now there is a
# black and white photo of you that is about to go viral. You cannot let this
# ruin your reputation, so you want to apply box blur algorithm to the photo
# to hide its content.
#
# The algorithm works as follows: each pixel x in the resulting image has a
# value equal to the average value of the input image pixels' values from the
# 3 × 3 square with the center at x. All pixels at the edges are cropped.
#
# As pixel's value is an integer, all fractions should be rounded down.
#
# Example
#
# For
#
# image = [[1, 1, 1],
#          [1, 7, 1],
#          [1, 1, 1]]
#
# the output should be boxBlur(image) = [[1]].


def boxBlur(image):

    my_array = image
    algo_array = []
    temp_array = []
    square = 0

    for n in range(len(my_array)-2):

        for i in range(len(my_array[0])-2):
            square = my_array[n][i] + my_array[n][i+1] + my_array[n][i+2]\
                   + my_array[n+1][i] + my_array[n+1][i+1] + my_array[n+1][i+2]\
                   + my_array[n+2][i] + my_array[n+2][i+1] + my_array[n+2][i+2]

            temp_array.append(square/9)

        algo_array.append(temp_array)
        temp_array = []

    return algo_array
