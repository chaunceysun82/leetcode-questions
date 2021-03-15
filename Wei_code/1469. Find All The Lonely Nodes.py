# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.res = []
        def helper(node):
            if not node:
                return
            if node and not node.left and node.right:
                self.res.append(node.right.val)
            if node and not node.right and node.left:
                self.res.append(node.left.val)
                
            helper(node.left)
            helper(node.right)
            
        helper(root)
        return self.res
                
        