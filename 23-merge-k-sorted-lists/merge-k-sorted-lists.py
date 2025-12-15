# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        for i, linkedlist in enumerate(lists):
            if linkedlist:
                heappush(pq, (linkedlist.val, i, linkedlist))

        dummy = ListNode()
        current = dummy
        while pq:
            _, i, node = heappop(pq)
            current.next = node
            current = current.next
            if node.next:
                heappush(pq, (node.next.val, i, node.next))
        return dummy.next
