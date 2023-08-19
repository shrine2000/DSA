# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        return self.merge_range(lists, 0, len(lists) - 1)
    
    def merge_range(self, lists, start, end):
        if start == end:
            return lists[start]
        
        mid = (start + end) // 2
        l = self.merge_range(lists, start, mid)
        r = self.merge_range(lists, mid + 1, end)
        
        return self.merge_two_lists(l, r)
    
    def merge_two_lists(self, l1, l2):
        dummy = ListNode()
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        current.next = l1 if l1 else l2
        
        return dummy.next