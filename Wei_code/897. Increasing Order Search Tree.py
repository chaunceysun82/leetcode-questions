# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root:
                inorder(root.left)
                root.left = None #why
                self.cur.right = root
                self.cur = self.cur.right
                inorder(root.right)
        dummy = TreeNode(0)
        self.cur = dummy
        inorder(root)
        return dummy.right