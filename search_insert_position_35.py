# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1
# Example 3:

# Input: [1,3,5,6], 7
# Output: 4
# Example 4:

# Input: [1,3,5,6], 0
# Output: 0

from typing import List


def search_insert(nums: List[int], target: int) -> int:
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (hi + lo) // 2
        mid_val = nums[mid]

        if target == mid_val:
            return mid
        elif target > mid_val:
             lo = mid + 1
        else:
            hi = mid - 1

    return lo
