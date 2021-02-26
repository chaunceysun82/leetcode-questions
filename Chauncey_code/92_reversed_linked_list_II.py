# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right or head.next is None:
            return head

        dummy_head = ListNode()
        dummy_head.next = head
        pre = dummy_head
        cur = head

        i = 1
        while i < left:
            pre = cur
            cur = cur.next
            i += 1

        temp_end = pre
        temp_start = cur
        post = cur.next

        while i < right:
            pre = cur
            cur = post
            post = post.next

            cur.next = pre
            i += 1

        temp_end.next = cur
        temp_start.next = post

        return dummy_head.next