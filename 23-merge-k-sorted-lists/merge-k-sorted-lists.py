# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i, head))
        dummy_head = ListNode()
        current = dummy_head

        while pq:
            val, list_idx, node = heapq.heappop(pq)
            current.next = node
            current = current.next
        
            if node.next:
                heapq.heappush(pq, (node.next.val, list_idx, node.next))

        return dummy_head.next

 