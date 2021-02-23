# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        if not s:
            return False

        if s.val == t.val and self.is_identical(s, t): 
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


    def is_identical(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        return self.is_identical(root1.left, root2.left) and self.is_identical(root1.right, root2.right)


