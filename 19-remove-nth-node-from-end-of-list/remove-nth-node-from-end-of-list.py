# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        idx = length - n
        if idx == 0:
            return head.next

        counter = 0
        curr = head
        while curr:
            if counter == idx - 1:
                if curr.next:
                    curr.next = curr.next.next
                break
            counter += 1
            curr = curr.next

        return head
