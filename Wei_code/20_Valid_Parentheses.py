class Solution:
    def isValid(self, s: str) -> bool:
        dict = {")": "(", "}": "{", "]": "["}
        
        stack = []
        
        for ch in s:
            if ch in dict:
                if stack ==[]:
                    return False
                if dict[ch] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
                
        return not stack