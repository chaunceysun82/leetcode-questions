# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf_list_1, leaf_list_2 = [],[]
        self.find_leaf_left_to_right(root1, leaf_list_1)
        self.find_leaf_left_to_right(root2, leaf_list_2)
        return leaf_list_1 == leaf_list_2


    def find_leaf_left_to_right(self, root, leaf_list):
        if root is None:
            return

        if root.left is None and root.right is None:
            leaf_list.append(root.val)
            return

        self.find_leaf_left_to_right(root.left, leaf_list)
        self.find_leaf_left_to_right(root.right, leaf_list)

        return leaf_list