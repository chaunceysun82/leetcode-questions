# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return

        if low <= root.val <= high:
            self.output += root.val

        if low < root.val:
            self.rangeSumBST(root.left, low, high)

        if root.val < high:
            self.rangeSumBST(root.right, low, high)

        return self.output