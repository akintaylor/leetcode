class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            number_two = target - nums[i]
            
            if number_two in hashmap:
                return [i, hashmap[number_two]]
            
            hashmap[nums[i]] = i
            