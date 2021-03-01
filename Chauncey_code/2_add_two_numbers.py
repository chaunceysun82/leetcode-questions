# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = ListNode(-1)
        cur = dummy
        carry = 0

        while l1 or l2:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            digit = (digit1 + digit2 + carry) % 10
            carry = (digit1 + digit2 + carry) // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            cur.next = ListNode(digit)
            cur = cur.next

        if carry > 0:
            cur.next = ListNode(carry)
            cur = cur.next

        cur.next = None

        return dummy.next