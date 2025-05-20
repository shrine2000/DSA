from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        return f"Node(value={self.val}, next={self.next})"


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        dummy = {}

        curr = head
        while curr:
            dummy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = dummy[curr]
            copy.next = dummy.get(curr.next)
            copy.random = dummy.get(curr.random)
            curr = curr.next
        return dummy[head]


def print_list(head):
    """Helper function to print the linked list in (val, random_val) format"""
    result = []
    visited = {}
    curr = head
    while curr:
        visited[curr] = curr
        random_val = curr.random.val if curr.random else None
        result.append(f"({curr.val}, random={random_val})")
        curr = curr.next
    return " -> ".join(result)


def test_copy_random_list():
    sol = Solution()

    nodes = [Node(i) for i in range(5)]
    for i in range(4):
        nodes[i].next = nodes[i + 1]
    nodes[0].random = nodes[4]  # 0 → 4
    nodes[1].random = nodes[3]  # 1 → 3
    nodes[2].random = None  # 2 → None
    nodes[3].random = nodes[1]  # 3 → 1
    nodes[4].random = nodes[0]  # 4 → 0

    head = nodes[0]
    copied = sol.copyRandomList(head)
    print("Original:", print_list(head))
    print("Copied  :", print_list(copied))
    print()


if __name__ == "__main__":
    test_copy_random_list()
