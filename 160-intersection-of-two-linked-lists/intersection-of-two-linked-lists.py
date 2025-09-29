# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        headAMap = {}

        tempA = headA
        while tempA:
            headAMap[tempA] = tempA.val
            tempA = tempA.next

        tempB = headB

        while tempB:
            if tempB in headAMap:
                return tempB
            tempB = tempB.next

        return None
