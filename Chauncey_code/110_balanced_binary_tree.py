# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        return self.helper(root, 0)[0]

    def helper(self, root, height):
        if root is None:
            return True, 0

        if root.left is None and root.right is None:
            return True, 1

        is_left_balanced, left_height  = self.helper(root.left, height + 1)
        is_right_balanced, right_height = self.helper(root.right, height + 1)

        return is_left_balanced and is_right_balanced and abs(left_height - right_height) <= 1, max(left_height, right_height) + 1