class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        list1 = []
        list2 = []
        
        for ch in num1:
            list1.append(int(ch))
            
        for ch in num2:
            list2.append(int(ch))
            
        n = len(list1)
        m = len(list2)
        
        number1 = number2 = 0
        
        for i in range(n):
            number1 += list1[i]*10**(n-1-i)
            
        for j in range(m):
            number2 += list2[j]*10**(m-1-j)
            
        sum = number1 + number2
        
        return str(sum)