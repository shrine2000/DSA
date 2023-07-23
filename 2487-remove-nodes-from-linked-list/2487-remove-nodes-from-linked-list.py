# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('inf'))
        stack = [dummy]
        
        current = head
        while current is not None:
            while stack[-1].val < current.val:
                stack.pop()
            stack[-1].next = current
            stack.append(current)
            current = current.next
        return dummy.next
        