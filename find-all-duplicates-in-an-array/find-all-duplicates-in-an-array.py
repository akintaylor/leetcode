class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        look_up = {}
        result = set()
        
        for num in nums:
            if num in look_up:
                look_up[num] += 1
            else:
                look_up[num] = 1
                
        for num in nums:
            if look_up[num] == 2:
                result.add(num)
                
        return result
    