class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        result = []
        
        window_sum, window_start = 0.0, 0
        
        for window_end in range(len(nums)):
            window_sum += nums[window_end]
            
            if window_end >= k - 1:
                result.append(window_sum / k)
                window_sum -= nums[window_start]
                window_start += 1
                
        return max(result)