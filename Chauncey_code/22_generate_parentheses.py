# BFS version Brute Force

from collections import deque
class Solution:
    def generateParenthesis(self, n):

        output = []
        queue = deque([''])

        while len(queue) > 0:
            subset = queue.popleft()
            for c in ['(', ')']:
                new_subset = subset + c
                queue.append(new_subset)
                if len(new_subset) == n * 2 and self.is_valid(new_subset):
                    output.append(new_subset)

            if len(new_subset) > n * 2:
                break

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


# DFS version check valid during recursion

class Solution2:
    def generateParenthesis(self, n):
        results = []
        self.dfs(0, 0, '', n, results)
        return results


    def dfs(self, left_count, right_count, subseq, n, results):
        if left_count > n or right_count > n:
            return

        if left_count < right_count:
            return

        if left_count == n and right_count == n:
            results.append(subseq)

        self.dfs(left_count + 1, right_count, subseq + '(', n, results)
        self.dfs(left_count, right_count + 1, subseq + ')', n, results)


obj = Solution2()
n = 3
print(obj.generateParenthesis(n))