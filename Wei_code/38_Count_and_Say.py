class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        last = self.countAndSay(n-1)
        
        curr = ""
        count = 1
        i = 1
        
        while i < len(last) + 1:
            if i < len(last) and last[i] == last[i-1]:
                count += 1
            else:
                curr +=str(count) + str(last[i-1])
                count = 1
            i += 1
            
        return curr