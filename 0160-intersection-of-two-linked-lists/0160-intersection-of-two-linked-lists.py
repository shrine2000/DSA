# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, head1: ListNode, head2: ListNode
    ) -> Optional[ListNode]:
        """
        Check if there is an intersection between two linked lists.

        Time Complexity: O(n + m), where n and m are the lengths of the two linked lists.
        Space Complexity: O(1).
        """

        # Handle edge cases where either of the lists is empty
        if not head1 or not head2:
            return None

        d1 = head1
        d2 = head2
        while d1 != d2:
            d1 = d1.next if d1 else head2
            d2 = d2.next if d2 else head1

        return d1
