class Solution:
    def reverse_number(self, number: int) -> int:
        result = 0
        
        while number > 0:
            number, remainder = divmod(number, 10)
            result = (result * 10) + remainder  
            
        return result  
    
            
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x <= 9:
            return True
        
        reversed_number = self.reverse_number(x)
        
        return reversed_number == x
    