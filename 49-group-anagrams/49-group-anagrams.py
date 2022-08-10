class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        result = []
        
        for string in strs:
            string_sorted = ''.join(sorted(string))
            
            if hashmap.get(string_sorted) is None:
                hashmap[string_sorted] = [string]
            else:
                hashmap[string_sorted].append(string)
                
        for anagram in hashmap.values():
            result.append(anagram)
            
        return result 
