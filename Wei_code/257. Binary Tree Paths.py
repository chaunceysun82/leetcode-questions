# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        def root_leaf(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)

                else:
                    path = path + '->' 
                    root_leaf(root.left, path)
                    root_leaf(root.right, path)
        
        paths = []
        root_leaf(root, '')
        return paths