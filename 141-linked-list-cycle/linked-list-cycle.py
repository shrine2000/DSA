# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        check = defaultdict(int)

        curr = head

        while curr:
            if check[curr] >= 1:
                return True
            check[curr] += 1
            curr = curr.next
        return False
