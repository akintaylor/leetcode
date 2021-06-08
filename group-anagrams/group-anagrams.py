class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        result = []
        
        for string in strs:
            string_sorted = ''.join(sorted(string))
            
            if string_sorted in ht:
                ht[string_sorted].append(string)
            else:
                ht[string_sorted] = [string]
            
        for group in ht.values():
            result.append(group)
        
        return result