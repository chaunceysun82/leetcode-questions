"""# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        root.left.val, root.right.val = root.right.val, root.left.val
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        
        root.left = left
        root.right = right
        
        return root"""

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        from queue import Queue
        
        if not root:
            return None
            
        que = Queue()
        que.put(root)
        
        while not que.empty():
            cur = que.get()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                que.put(cur.left)
            if cur.right:
                que.put(cur.right)
                
        return root