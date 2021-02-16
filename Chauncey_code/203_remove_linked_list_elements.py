# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        prev, cur = dummy, head
        while cur:
            if cur.val == val:
                cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next

        return dummy.next