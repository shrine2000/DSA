# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        
        odd_values = []
        even_values = []
        current = head
        count = 1

        while current:
            if count % 2 == 1:
                odd_values.append(current.val)
            else:
                even_values.append(current.val)
            count += 1
            current = current.next

        values = odd_values + even_values

        new_head = ListNode(values[0])
        current = new_head

        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next

        return new_head