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

        prev, node = None, leaf
        while node != root:
            if prev == node.right:
                node.right = node.left
            node.left = node.parent

            node.parent, node, prev = prev, node.parent, node

        if prev == node.right:
            node.right = None
        else:
            node.left = None
        node.parent = prev

        return leaf