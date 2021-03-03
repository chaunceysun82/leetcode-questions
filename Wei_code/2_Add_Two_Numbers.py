# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        curr = ListNode(0)
        dummy = ListNode(-1, curr)
        prev = dummy
        carry = 0
        while l1 or l2 or carry:
            value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            curr = ListNode(value % 10)
            carry = value // 10
            prev.next = curr
            prev = prev.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        if l1 and not l2:
            perv.next = l2
            
        if l2 and not l1:
            perv.next = l1
            
        return dummy.next
            
            
            
            
        