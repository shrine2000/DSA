# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
            while b:
                a, b = b, a % b
            return a
        
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            gcd = self.gcd(head.val, head.next.val)
            
            new_node = ListNode(gcd)
            new_node.next = head.next
            head.next = new_node
            
            prev = new_node.next
            head = prev
            
        return dummy.next
        
        