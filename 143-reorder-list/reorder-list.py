# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = fast = head

        # find mid of the list

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow

        # reverse the second half
        # save reverse move move
        prev, curr = None, mid

        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr # not sure
            curr = curr_next


        # interleave both halfs
        first = head
        second = prev

        while second.next:
            nxt1 = first.next
            nxt2 = second.next

            first.next = second
            second.next = nxt1

            first = nxt1
            second = nxt2

