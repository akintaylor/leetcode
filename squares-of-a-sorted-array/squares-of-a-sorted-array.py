class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_squares = [0] * len(nums)
        
        smaller_value_idx = 0
        larger_value_idx = len(nums) - 1
        
        for idx in reversed(range(len(nums))):
            smaller_value = nums[smaller_value_idx]
            larger_value = nums[larger_value_idx]
            
            if abs(smaller_value) > abs(larger_value):
                sorted_squares[idx] = smaller_value ** 2
                smaller_value_idx += 1
            else:
                sorted_squares[idx] = larger_value ** 2
                larger_value_idx -= 1
                
        return sorted_squares