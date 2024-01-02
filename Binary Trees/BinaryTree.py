from typing import Optional


class Node:
    def __init__(self, key: int) -> None:
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.val: int = key


class BinaryTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, root: Optional[Node], key: int) -> Node:
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def inorder_traversal(self, root: Optional[Node]) -> None:
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = tree.insert(tree.root, 50)
    tree.insert(tree.root, 30)
    tree.insert(tree.root, 20)
    tree.insert(tree.root, 40)
    tree.insert(tree.root, 70)
    tree.insert(tree.root, 60)
    tree.insert(tree.root, 80)

    print("Inorder Traversal of the constructed binary tree:")
    tree.inorder_traversal(tree.root)
