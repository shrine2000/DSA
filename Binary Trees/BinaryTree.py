from collections import deque


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree(self, nodes):
        # Build a binary tree from a list of nodes
        node_dict = {}
        for value, left, right in nodes:
            node = node_dict.get(value, TreeNode(value))
            node_dict[value] = node

            if left:
                left_node = node_dict.get(left, TreeNode(left))
                node.left = left_node
                node_dict[left] = left_node

            if right:
                right_node = node_dict.get(right, TreeNode(right))
                node.right = right_node
                node_dict[right] = right_node

        self.root = node_dict[nodes[0][0]]

    def preorder_recursive(self, root):
        # Pre-order traversal (recursive)
        if root:
            print(root.val, end=" ")
            self.preorder_recursive(root.left)
            self.preorder_recursive(root.right)

    def inorder_recursive(self, root):
        # In-order traversal (recursive)
        if root:
            self.inorder_recursive(root.left)
            print(root.val, end=" ")
            self.inorder_recursive(root.right)

    def postorder_recursive(self, root):
        # Post-order traversal (recursive)
        if root:
            self.postorder_recursive(root.left)
            self.postorder_recursive(root.right)
            print(root.val, end=" ")

    def level_order(self):
        # Level-order traversal (using queue)
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result

    def preorder_iterative(self):
        # Iterative pre-order traversal (using stack)
        if not self.root:
            return []

        result = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def inorder_iterative(self):
        # Iterative in-order traversal (using stack)
        if not self.root:
            return []

        result = []
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result


# Example usage
if __name__ == "__main__":
    # Create a tree and specify the nodes (value, left child, right child)
    tree = BinaryTree()
    nodes = [
        (1, 2, 3),
        (2, 4, 5),
        (3, 6, 7),
        (4, None, None),
        (5, None, None),
        (6, None, None),
        (7, None, None),
    ]
    tree.build_tree(nodes)

    # Print various traversal results
    print("Pre-order Recursive:")
    tree.preorder_recursive(tree.root)
    print("\n")

    print("In-order Recursive:")
    tree.inorder_recursive(tree.root)
    print("\n")

    print("Post-order Recursive:")
    tree.postorder_recursive(tree.root)
    print("\n")

    print("Level-order:")
    print(tree.level_order())
    print("\n")

    print("Iterative Pre-order:")
    print(tree.preorder_iterative())
    print("\n")

    print("Iterative In-order:")
    print(tree.inorder_iterative())
