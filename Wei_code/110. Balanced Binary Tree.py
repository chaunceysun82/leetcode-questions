# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return -1 <= self.maxDepth(root.left) - self.maxDepth(root.right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
        
        
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
        