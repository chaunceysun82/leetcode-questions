"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        prev = None
        cur = leaf
        while cur != root:
            if cur.left != prev:
                cur.right = cur.left
            cur.left = cur.parent
            
            cur.parent, cur, prev = prev, cur.parent, cur
            
        if prev == cur.right:
            cur.right = None
            
        else:
            cur.left = None
            
        cur.parent = prev
        
        return leaf