class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        num_sum = sum(nums)
        
        real_sum = 0
        
        for i in range(n + 1):
            real_sum += i
        
        return real_sum - num_sum
    