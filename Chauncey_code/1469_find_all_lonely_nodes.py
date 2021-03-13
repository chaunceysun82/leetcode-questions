# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.res = []
        self.helper(root)

        return self.res

    def helper(self, node):
        if node is None:
            return

        if node.left and not node.right:
            self.res.append(node.left.val)

        if node.right and not node.left:
            self.res.append(node.right.val)

        self.helper(node.left)
        self.helper(node.right)