# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next

        return self.convert_arr_to_BST(nums, 0, len(nums) - 1)


    def convert_arr_to_BST(self, nums, start, end):
        if start > end:
            return
        mid = (start + end) // 2

        root = TreeNode(nums[mid])
        root.left = self.convert_arr_to_BST(nums, start, mid - 1)
        root.right = self.convert_arr_to_BST(nums, mid + 1, end)

        return root