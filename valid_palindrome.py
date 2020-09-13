# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false


# Constraints:
# s consists only of printable ASCII characters.


# solution 1
def is_palindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower()

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1

    return True


# solution 2
def is_palindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, str)).lower()
    return ''.join(reversed(s)) == s
