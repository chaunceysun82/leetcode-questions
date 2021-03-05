# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root:
            return depth
        
        else:
            depth = 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
            
        return depth
#         else:
#             left = self.maxDepth(root.left)
#             right = self.maxDepth(root.right)
            
#             return max(left, right) +1
    
        