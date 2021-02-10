class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        sign = x/abs(x)
        
        list = []
        newlist = []
        stringx = str(abs(x))
        
        for ch in stringx:
            list.append(ch)
        
        while list:
            newlist.append(int(list.pop()))
            
        reversed_s = 0
        n = len(newlist)
        for i in range(n):
            reversed_s += newlist[i]*10**(n-1-i)
        
        reversed_s = int(reversed_s*sign)
        
        if -2**31 <= reversed_s <= 2**31 - 1:
            return reversed_s
        else:
            return 0