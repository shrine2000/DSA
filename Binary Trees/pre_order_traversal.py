class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def preorder_traversal_iterative(self, root):
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node: TreeNode = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def pre_order_traversal_recursive(self, root):
        def traverse(node: TreeNode, result):
            if node is None:
                return
            result.append(node.val)
            traverse(node.left, result)
            traverse(node.right, result)

        traversal_result = []
        traverse(root, traversal_result)
        return traversal_result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    tree = TreeNode(None)

    iterative_result = tree.preorder_traversal_iterative(root)
    print("Preorder Traversal (Iterative):", iterative_result)

    recursive_result = tree.pre_order_traversal_recursive(root)
    print("Preorder Traversal (Recursive):", recursive_result)
