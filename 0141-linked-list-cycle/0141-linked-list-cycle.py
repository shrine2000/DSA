# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is not None and head.next is None:
            return False
        
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False
    
    """
    Here's how the hasCycle method works:

    First, the method checks if the head node is None or the list has only one node. In these cases, there can't be a cycle, so it returns False.

    The method initializes two pointers, slow and fast, to the head node.

    The method uses a while loop to move the fast pointer two steps ahead and the slow pointer one step ahead in each iteration. If there is a cycle in the list, the fast pointer will eventually catch up with the slow pointer.

    Inside the loop, the method checks if the slow pointer and fast pointer meet. If they meet, it means there is a cycle in the list, so it returns True.

    If the loop terminates without finding a cycle, it means the fast pointer reached the end of the list, and there is no cycle. In this case, it returns False.
    
    """