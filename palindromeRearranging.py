# Given a string, find out if its characters can be rearranged
# to form a palindrome.

# Example

# For inputString = "aabb", the output should be
# alindromeRearranging(inputString) = true.

# We can rearrange "aabb" to make "abba", which is a palindrome.


def palindromeRearranging(inputString):

    to_check = list(inputString)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_soup = list(alphabet)
    odds = 0

    for i in iter(alphabet_soup):
        if to_check.count(i) % 2 != 0:
            odds += 1

    if odds <= 1:
        return True
    else:
        return False
