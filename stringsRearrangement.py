# Given an array of equal-length strings, check if it is possible to
# rearrange the strings in such a way that after the rearrangement the strings
# at consecutive positions would differ by exactly one character.
#
# Example
#
# For inputArray = ["aba", "bbb", "bab"], the output should be
# stringsRearrangement(inputArray) = false;
#
# All rearrangements don't satisfy the description condition.
#
# For inputArray = ["ab", "bb", "aa"], the output should be
# stringsRearrangement(inputArray) = true.
#
# Strings can be rearranged in the following way: "aa", "ab", "bb".


from itertools import permutations

def stringsRearrangement(inputArray):

    new_array = {}
    new_array2 = {}
    possible_sequences = [x for x in permutations(inputArray)]
    valid = False

    # Get the ord for each value and add it to a dictionary of tuples
    # Ex. inputArray = inputArray = ["aa", "ab", "bb"]
    # becomes... {'aa': (97, 97), 'ab': (97, 98), 'bb': (98, 98)}
    for x in inputArray:
        temp = []
        for y in list(x):
            temp.append(ord(y))
        new_array[x] = tuple(temp)

    # Create a new dictionary (new_array2) that now shows key-value pairings, where
    # the keys are unchanged but the values represent the keys of valid adjacencies
    # according to the sequence rules. Ex. the example above becomes...
    # {
    #     'aa': ['ab'],
    #     'ab': ['aa', 'bb'],
    #     'bb': ['ab']
    # }

    # THIS IS WHERE THE CURRENT TEST IS FAILING!
    for key1 in new_array:
        temp = []
        add_to_dict = []
        for key2 in new_array:
            temp = [abs(x - y) for x, y in zip(list(new_array[key1]), list(new_array[key2]))]
            if temp.count(0) == len(key1) - 1:
                add_to_dict.append(key2)
        new_array2[key1] = add_to_dict

    # For each possible sequence, check to see whether it's valid based on new_array2
    # After finding one that is, return True, else run to the end and return False
    for x in possible_sequences:
        for i, y in enumerate(x):
            if i == len(x)-1:
                valid = True
                break
            elif x[i+1] in new_array2.get(y):
                pass
            else:
                break

    return valid
