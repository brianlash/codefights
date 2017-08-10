# You are given an array of desired filenames in the order of their creation.
# Since two files cannot have equal names, the one which comes later
# will have an addition to its name in a form of (k), where k is the
# smallest positive integer such that the obtained name is not used yet.
#
# Return an array of names that will be given to the files.


def fileNaming(names):

    new_list = []
    temp_count = 0
    keep_trying = True

    for x in range(len(names)):
        temp_count = new_list.count(names[x])
        if temp_count == 0:
            new_list.append(names[x])
        else:
            while True:
                candidate = names[x] + '(' + str(temp_count) + ')'
                if new_list.count(candidate) == 0:
                    new_list.append(candidate)
                    break
                else:
                    temp_count += 1

    return new_list
