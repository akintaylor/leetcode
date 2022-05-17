class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        lookup = {}
        
        for c in s:
            if c in lookup:
                lookup[c] += 1
            else:
                lookup[c] = 1
        
        for c in t:
            if c in lookup and lookup[c] >= 1:
                lookup[c] -= 1
                if lookup[c] == 0:
                    lookup.pop(c)
        
        return len(lookup) == 0