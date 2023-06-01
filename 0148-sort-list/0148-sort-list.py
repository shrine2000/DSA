# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        def merge(left, right):
            dummy = ListNode(0)
            curr = dummy
            
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
                
                
            curr.next = left if left else right
            
            return dummy.next
        
        def split(head):
            slow = head
            fast = head.next
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
            second_half = slow.next
            slow.next = None
            
            return head, second_half
        
        left, right = split(head)
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)
        
        return merge(left_sorted, right_sorted)
    
# Time complexity: O(n log n) - where n is the number of nodes in the linked list
# Space complexity: O(log n) - for the recursive stack space during function calls