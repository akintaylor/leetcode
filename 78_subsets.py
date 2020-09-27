# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# Solution 1
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    queue = [[]]

    for num in nums:
        sz = len(queue)
        for cur in queue:
            if sz == 0:
                break
            copy = cur[:]
            copy.append(num)
            queue.append(copy)
            sz -= 1

    return queue


# Solution 2

def subsets(nums: List[int]) -> List[List[int]]:
    queue = [[]]

    for num in nums:
        queue += [cur + [num] for cur in queue]

    return queue
