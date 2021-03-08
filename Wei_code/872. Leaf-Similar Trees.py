# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def helper(leaf_list, root):
            if not root:
                return

            if not root.left and not root.right:
                leaf_list.append(root.val)

            helper(leaf_list, root.left)
            helper(leaf_list, root.right)
        
        leaf_list1 = []
        leaf_list2 = []
        helper(leaf_list1, root1)
        helper(leaf_list2, root2)
        return leaf_list1 == leaf_list2