# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node or not node.next: 
            return 
        
        node.val = node.next.val
        
        node.next = node.next.next
        
        
        """
        
        The code proceeds to delete the node in-place by copying the value of the next node to the current node, which effectively replaces the current node with the next node. Subsequently, it updates the current node's next pointer to skip the next node, thereby effectively removing it from the linked list.
        
        """
        
        