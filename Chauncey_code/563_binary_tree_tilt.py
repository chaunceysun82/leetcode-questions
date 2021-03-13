# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.tilt_sum = 0
        _, tilt_root = self.helper(root)
        self.tilt_sum += tilt_root

        return self.tilt_sum


    def helper(self, root):
        if root is None:
            return 0, 0

        if root.left is None and root.right is None:
            return root.val, 0

        node_sum_left, tilt_left_node = self.helper(root.left)
        node_sum_right, tilt_right_node = self.helper(root.right)

        node_sum = node_sum_left + root.val + node_sum_right
        tilt_node = abs(node_sum_left - node_sum_right)
        self.tilt_sum += tilt_left_node + tilt_right_node

        return node_sum, tilt_node