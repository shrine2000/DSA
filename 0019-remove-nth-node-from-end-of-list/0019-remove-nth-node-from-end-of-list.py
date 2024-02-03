# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        if n == length:
            return head.next

        prev = None
        current = head
        count = 0
        while current:
            if count == length - n:
                break

            count += 1
            prev = current
            current = current.next

        prev.next = current.next

        return head
