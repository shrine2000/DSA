# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        
        while head:
            values.append(head.val)
            head = head.next
        
        if not values:
            return None
        
        new_head = ListNode(values.pop())
        current = new_head
        
        while values:
            current.next = ListNode(values.pop())
            current = current.next
        
        return new_head