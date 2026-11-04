# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow = fast = head

        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if slow is fast:
        #         return True
        # return False

        visited = set()
        curr = head
        while curr:
            next_node = curr.next
            if next_node in visited:
                return True
            visited.add(next_node)
            curr = curr.next
        return False
