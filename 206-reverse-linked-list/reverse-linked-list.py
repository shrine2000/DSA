# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        #SAVE -> REVERSE -> MOVE -> MOVE. Return prev (new head), not next_node.

        prev = None
        curr = head

        while curr:
            next_node = curr.next  # SAVE
            curr.next = prev       # REVERSE
            prev = curr            # MOVE prev
            curr = next_node       # MOVE curr

        return prev
        