# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy_head = TreeNode(-1)
        self.prev = dummy_head
        self.inorder_traverse(root)
        return dummy_head.right

    def inorder_traverse(self, root):
        if root is None:
            return

        self.inorder_traverse(root.left)
        root.left = None
        self.prev.right = root
        self.prev = root
        self.inorder_traverse(root.right)