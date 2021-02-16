# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.get_longest_path(root)[1] -1    # diamater = longest_path - 1

    def get_longest_path(self, root):
        if not root:
            return 0, 0

        left_h, left_longest_path = self.get_longest_path(root.left)
        right_h, right_longest_path = self.get_longest_path(root.right)

        height = max(left_h, right_h) + 1
        longest_path = max(left_h + right_h + 1, left_longest_path, right_longest_path)

        return height, longest_path