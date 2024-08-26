
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        n = 0
        curr = head
        tail = None
        while curr:
            n += 1
            if not curr.next:
                tail = curr
            curr = curr.next
            
        tail.next = head
        
        k = k % n 
        steps_to_new_head = n - k
        new_tail = head
        
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
