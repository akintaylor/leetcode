# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []


# Constraints:

# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import List


def three_suum(nums: List[int]) -> List[List[int]]:
    output = []
    nums.sort()
    length = len(nums)

    for i in range(length):
        left, right = i + 1, length - 1
        if i > 0 and nums[i-1] == nums[i]:
            continue
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                output.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left+1] == nums[left]:
                    left += 1
                while left < right and nums[right-1] == nums[right]:
                    right -= 1
                left += 1
                right -= 1
            elif total > 0:
                right -= 1
            else:
                left += 1

    return output
