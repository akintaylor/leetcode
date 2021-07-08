class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        look_up = {}
        
        for num in nums:
            if num in look_up:
                look_up[num] += 1
            else:
                look_up[num] = 1
                
        for num in nums:
            if look_up[num] == 1:
                return num