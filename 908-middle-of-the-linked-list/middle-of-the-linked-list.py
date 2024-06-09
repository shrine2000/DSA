# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        
        n = len(nodes)
        mid = n // 2
        
        return nodes[mid]

            
            
        