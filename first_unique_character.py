# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.


# Note: You may assume the string contains only lowercase English letters.

def first_unique_character(s):
    char_frequency = {}

    for char in s:
        if char_frequency.get(char):
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    for i, char in enumerate(s):
        if char_frequency.get(char) == 1:
            return i

    return -1
