"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                for child in cur.children:
                    queue.append(child)

            depth += 1

        return depth