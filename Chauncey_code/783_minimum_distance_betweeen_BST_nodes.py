# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.min_diff = float('inf')
        self.prev = float('-inf')
        self.inorder_traverse(root)
        return self.min_diff

    def inorder_traverse(self, root):
        if root is None:
            return

        self.inorder_traverse(root.left)
        self.min_diff = min(self.min_diff, root.val - self.prev)
        self.prev = root.val
        self.inorder_traverse(root.right)
