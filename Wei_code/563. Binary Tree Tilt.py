# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.tilt = 0
        def dfs(root):
            if not root:
                return 0
            
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            self.tilt += abs(left_sum - right_sum)
            
            return left_sum + right_sum + root.val
        
        dfs(root)
        
        return self.tilt
        