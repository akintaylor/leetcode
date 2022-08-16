class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        char_set = set()
        l, r = 0, 0
        longest = 0
        
        while r < len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])
            longest = max(r - l + 1, longest)
            r += 1
        
        return longest
