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
        val_list = []
        
        while head:
            val_list.append(head.val)
            head = head.next
        
            
        def list_to_tree(lis):
            if not lis:
                return None

            mid = len(lis)//2
            root = TreeNode(lis[mid])
            root.left = list_to_tree(lis[:mid])
            root.right = list_to_tree(lis[mid+1:])

            return root
        
        return list_to_tree(val_list)
        