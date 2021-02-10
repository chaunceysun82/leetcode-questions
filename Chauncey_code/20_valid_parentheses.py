class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) % 2 == 1:
        #     return False

        stack = []

        for ch in s:
            if stack and stack[-1] + ch in ['()', '[]', '{}']:
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0