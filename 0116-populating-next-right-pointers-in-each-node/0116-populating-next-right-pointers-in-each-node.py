from collections import deque


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# https://www.youtube.com/watch?v=FrD3_PXwhj0
class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i < level_size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


if __name__ == "__main__":
    # Example usage:
    # Construct the binary tree
    #        1
    #       / \
    #      2   3
    #     / \   \
    #    4   5   7

    node7 = Node(7)
    node5 = Node(5)
    node4 = Node(4)
    node3 = Node(3, None, node7)
    node2 = Node(2, node4, node5)
    root = Node(1, node2, node3)

    solution = Solution()
    solution.connect(root)

    # The tree should now be connected as:
    #        1 -> None
    #       / \
    #      2 -> 3 -> None
    #     / \    \
    #    4-> 5 -> 7 -> None

    # Print connections
    def print_connections(node):
        while node:
            curr = node
            while curr:
                print(curr.val, end=" -> ")
                curr = curr.next
            print("None")
            node = node.left

    print_connections(root)
