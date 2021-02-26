from collections import deque
class Solution:
    def generateParenthesis(self, n):

        output = []
        queue = deque([''])
        index = 0

        while index < 2 ** (n * 2) - 1:
            subset = queue.popleft()
            index += 1
            for c in ['(', ')']:
                new_subset = subset + c
                queue.append(new_subset)
                if len(new_subset) == 6 and self.is_valid(new_subset):
                    output.append(new_subset)

        return output

    def is_valid(self, s):
        stack = []

        for ch in s:
            if stack and stack[-1] + ch == '()':
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0


obj = Solution()
n = 3
print(obj.generateParenthesis(n))