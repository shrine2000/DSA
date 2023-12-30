class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head = self.reverseLinkedList(head)
        
        current_node = reversed_head
        carry = 0
        while current_node:
            new_value = (current_node.val * 2)
            current_node.val = (new_value % 10) + carry
            carry = new_value // 10
            previous_node = current_node
            current_node = current_node.next
        if carry:
            print(carry, previous_node, current_node)
            previous_node.next = ListNode(carry)
        
        return self.reverseLinkedList(reversed_head)
    
    def reverseLinkedList(self, head):
        previous_node, next_node = None, None
        current_node = head
        
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        
        return previous_node