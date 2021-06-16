class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self._is_valid(s[(i+1):(j+1)]) or self._is_valid(s[i:j])
        return True
    
    def _is_valid(self, s):
        return s == s[::-1]