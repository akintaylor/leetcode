class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_table = {}
        
        for index, value in enumerate(nums):
            complement = target - nums[index]
            
            if complement in lookup_table:
                return [index, lookup_table[complement]]
            
            lookup_table[nums[index]] = index