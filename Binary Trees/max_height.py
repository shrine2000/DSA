# https://www.geeksforgeeks.org/find-the-maximum-depth-or-height-of-a-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def max_depth(self, node: "Node") -> int:
        """
        Recursive function to find the height (max depth) of a binary tree.

        Args:
        - node: Root node of the binary tree.

        Returns:
        - int: Height of the binary tree.
        """
        # Base case: If the node is None, the height is 0.
        if node is None:
            return 0

        # Recursively calculate the height of the left subtree.
        left_depth = self.max_depth(node.left)

        # Recursively calculate the height of the right subtree.
        right_depth = self.max_depth(node.right)

        # The height of the current node is the maximum depth of its subtrees plus 1.
        current_depth = max(left_depth, right_depth) + 1

        return current_depth


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

tree_height = root.max_depth(root)
print("Height of the binary tree:", tree_height)
