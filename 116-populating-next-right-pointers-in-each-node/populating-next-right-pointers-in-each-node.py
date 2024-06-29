"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        current = root
        while current.left:
            next_level = current.left
            while current:
                current.left.next = current.right
                if current.next:
                    current.right.next = current.next.left
                current = current.next
            current = next_level
        return root