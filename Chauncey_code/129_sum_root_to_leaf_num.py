# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        queue = collections.deque([(root, str(root.val))])

        while len(queue) > 0:
            node, path = queue.popleft()
            if node.left is None and node.right is None:
                res.append(path)
            if node.left:
                queue.append((node.left, path + str(node.left.val)))
            if node.right:
                queue.append((node.right, path + str(node.right.val)))

        total_sum = 0
        for ch in res:
            total_sum += int(ch)

        return total_sum



class Solution2:
    def sumNumbers(self, root: TreeNode) -> int:
        total_sum = 0
        stack = [(root, 0)]

        while stack:
            node, cur_val = stack.pop()
            if node:
                cur_val = cur_val * 10 + node.val

                if node.left is None and node.right is None:
                    total_sum += cur_val

                else:
                    stack.append((node.left, cur_val))
                    stack.append((node.right, cur_val))

        return total_sum