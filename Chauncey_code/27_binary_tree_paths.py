# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution1:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)

        res = []

        for path in left_paths + right_paths:
            res.append(str(root.val) + '->' + path)

        return res




class Solution2:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        res = []

        return self.dfs(root, '', res)


    def dfs(self, root, path, res):
        if root.left is None and root.right is None:
            res.append(path + str(root.val))
            return

        new_path = path + str(root.val) + '->'

        if root.left:
            self.dfs(root.left, new_path, res)
        if root.right:
            self.dfs(root.right, new_path, res)

        return res