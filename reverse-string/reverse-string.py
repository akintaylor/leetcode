class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end = len(s) - 1
        start = 0
        
        while start < end:
            s[end], s[start] = s[start], s[end]
            start += 1
            end -= 1
            
        
            