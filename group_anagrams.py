# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.

from typing import List


def group_anagrams(self, strs: List[str]) -> List[List[str]]:
    groups = {}

    for string in strs:
        sorted_string = ''.join(sorted(string))
        if groups.get(sorted_string):
            groups[sorted_string].append(string)
        else:
            groups[sorted_string] = [string]

    return groups.values()
