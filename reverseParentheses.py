def reverseParentheses(s):

# Input: "The ((quick (brown) (fox) jumps over the lazy) dog)"
# Output: "The ((quick nworb xof jumps over the lazy) dog)"
# Output: "The (yzal eht revo spmuj fox brown kciuq dog)"
# Output: "The god quick nworb xof jumps over the lazy"

# Find the location of the last open paren
# Reverse everything between it and the next closure

    my_list = list(s)

    passes = my_list.count('(')
    completed = 0

    new_list = []
    abbreviated = []

    ## pass that many times
    while completed != passes:
        last_open = max([n for n, i in enumerate(my_list) if i == '('])
        first_close = min([n for n, i in enumerate(my_list) if i == ')' and n > last_open])

        new_list = my_list[last_open+1:first_close]

        for i in reversed(new_list):
            abbreviated.append(i)

        my_list[last_open+1:first_close] = abbreviated

        my_list.pop(last_open)
        my_list.pop(first_close-1)

        abbreviated = []
        completed += 1

    my_list = ''.join(my_list)

    return my_list

    ## last step, need to put list back to string

s = "a(bcdefghijkl(mno)p)q"

reverseParentheses(s)

# Expected Output:
# "apmnolkjihgfedcbq"
