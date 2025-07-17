# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []

        for lst in lists:
            while lst:
                res.append(lst)
                lst = lst.next
                
        if not res:
            return None
        
        res.sort(key=lambda node: node.val)
        for i in range(len(res) - 1):
            res[i].next = res[i + 1]
        res[-1].next = None


        return res[0]