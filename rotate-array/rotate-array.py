class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = k
        
        while count > 0:
            temp = nums.pop()
            nums.insert(0, temp)
            count -= 1
            