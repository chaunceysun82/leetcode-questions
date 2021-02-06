# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Three pointers
        # Time: O(n)
        # Space: O(1)

        if not head:
            return None
        if not head.next:
            return head

        left, mid, right = None, head, head.next

        while right:
            mid.next = left
            left = mid
            mid = right
            right = right.next

        mid.next = left

        return mid