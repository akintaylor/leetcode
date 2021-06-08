class Solution:
    def combine(self, i, cur, digits, result, digits_to_char):
        if len(cur) == len(digits):
            result.append(cur)
            return
        
        for c in digits_to_char[digits[i]]:
            self.combine(i + 1, cur + c, digits, result, digits_to_char)
        
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        
        digits_to_char = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        if digits:
            self.combine(0, '', digits, result, digits_to_char)
        
        return result
        
        