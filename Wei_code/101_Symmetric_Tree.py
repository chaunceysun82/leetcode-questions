# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root.left is None and root.right is None:
            return True
        
        return self.isSametree(root.left, root.right)
        
        
    def isSametree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        return self.isSametree(root1.right, root2.left) and self.isSametree(root1.left,root2.right)
        