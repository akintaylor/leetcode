class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = set(nums)
        
        print(result)
        
        return len(result) != len(nums)