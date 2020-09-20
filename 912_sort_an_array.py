# Given an array of integers nums, sort the array in ascending order.

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]


# Constraints:

# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000

from typing import List


def sort_array(nums: List[int]) -> List[int]:
    return merge_sort(nums)


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    block = []
    l_pointer = r_pointer = 0

    while l_pointer < len(left) and r_pointer < len(right):
        if left[l_pointer] < right[r_pointer]:
            block.append(left[l_pointer])
            l_pointer += 1
        else:
            block.append(right[r_pointer])
            r_pointer += 1

    if l_pointer < len(left):
        block += left[l_pointer:]
    elif r_pointer < len(right):
        block += right[r_pointer:]

    return block
