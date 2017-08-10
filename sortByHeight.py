# Some people are standing in a row in a park. There are trees between them
# which cannot be moved. Your task is to rearrange the people by their heights
# in a non-descending order without moving the trees.

# Example

# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].


def sortByHeight(a):

    my_list = a
    to_resort = []
    final_list = []

    for i in my_list:
        if i != -1:
            to_resort.append(i)

    to_resort = sorted(to_resort, reverse=True)

    for i in my_list:
        if i != -1:
            final_list.append(to_resort.pop())
        else:
            final_list.append(-1)

    return final_list
