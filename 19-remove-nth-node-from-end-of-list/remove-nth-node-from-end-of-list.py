# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head)
            head = head.next
        stack.pop(len(stack) - n)
        out, prev = None, None
        while stack:
            out = stack.pop()
            out.next = prev
            prev = out
        return out
