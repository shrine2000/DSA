class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None

class Solution:
    def removeDuplicates(self, head: Node) -> Node:
        current = head

        while current is not None and current.next is not None:
            if current.data == current.next.data:
                next_node = current.next
                current.next = next_node.next
                if next_node.next is not None:
                    next_node.next.prev = current
            else:
                current = current.next

        return head
