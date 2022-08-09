class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        
        if len(s) != len(t):
            return False
        
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 0
                
        for char in t:
            if char in hashmap:
                if hashmap[char] == 0:
                    hashmap.pop(char)
                else:
                    hashmap[char] -= 1
        
        return True if len(hashmap) == 0 else False
