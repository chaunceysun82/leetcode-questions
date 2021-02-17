# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.is_mirrored(root.left, root.right)

    def is_mirrored(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val == root2.val:
            return self.is_mirrored(root1.left, root2.right) and self.is_mirrored(root1.right, root2.left)