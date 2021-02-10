# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head  is None:
            return True
        
        stack = []
        curr = head
        
        while curr:
            stack.append(curr.val)
            curr = curr.next
            
        for i in range(len(stack)):
            print(f"stack[{i}]={stack[i]}, stack[{-1-i}]={stack[-1-i]}")
            if stack[i] != stack[-1-i]:
                return False
            
        return True
l = ListNode(1, ListNode(1, ListNode(2, ListNode(1))))
print(Solution().isPalindrome(l))