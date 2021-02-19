# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_d = [0]
        
        def dfs(node):
            if not node:
                return -1
            
            right = dfs(node.right)
            left = dfs(node.left)
            
            max_d[0] = max(max_d[0], left + right + 2)
            height = max(left, right) + 1
            return max(left, right) + 1
            
        dfs(root)
        return max_d[0]
        
        