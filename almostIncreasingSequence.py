# Given a sequence of integers as an array, determine whether it is possible
# to obtain a strictly increasing sequence by removing
# no more than one element from the array.

# For sequence = [1, 3, 2, 1], the output should be
# almostIncreasingSequence(sequence) = false;

# There is no one element in this array that can be removed in order to get a strictly increasing sequence.


def almostIncreasingSequence(sequence):

# for each number in sequence, compare it to the one after
# when one breaks the rule, remove it and start to loop again

    my_list = sequence

    for index, i in enumerate(my_list):
        try:
            if i >= my_list[index+1] and i < my_list[index+2]:
                del my_list[index+1]
                for index, i in enumerate(my_list):
                    try:
                        if i >= my_list[index+1]:
                            return False
                    except:
                        return True
            elif i >= my_list[index+1] and i >= my_list[index+2]:
                del my_list[index]
                for index, i in enumerate(my_list):
                    try:
                        if i >= my_list[index+1]:
                            return False
                    except:
                        return True
        except:
            return True
