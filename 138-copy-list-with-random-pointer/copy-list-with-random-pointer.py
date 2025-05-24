"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr=head
        while curr:
            new_node= Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr=new_node.next

        curr=head
        while curr:
            if curr.random:
                curr.next.random=curr.random.next
            curr=curr.next.next

        curr=head
        pseudo_head=Node(0)
        copy_curr=pseudo_head
        while curr:
            copy=curr.next
            curr.next=copy.next
            copy_curr.next=copy
            copy_curr=copy
            curr=curr.next
        return pseudo_head.next

        


