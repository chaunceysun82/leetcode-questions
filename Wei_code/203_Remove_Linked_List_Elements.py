# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0,head)
        curr = head
        prev = dummy
        
        while curr:
            if curr.val == val:
                curr = curr.next
                prev.next = curr
            else:
                curr = curr.next
                prev = prev.next
                
        return dummy.next
            