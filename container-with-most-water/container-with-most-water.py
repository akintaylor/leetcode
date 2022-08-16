class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        
        max_area = float('-inf')
        
        while left < right:
            left_height = height[left]
            right_height = height[right]
            
            min_height = min(left_height, right_height)
            width = right - left
            
            max_area = max(min_height * width, max_area)
            
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return max_area
            