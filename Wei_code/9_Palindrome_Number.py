class Solution:
    def isPalindrome(self, x: int) -> bool:
        #return str(x) == str(x)[::-1]
        
        if x < 0:
            return False
        
        reversed_x = 0
        temp = x

        while temp > 0:
            reversed_x = reversed_x*10 + temp%10
            temp = temp//10
            
        return x == reversed_x