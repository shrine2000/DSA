from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string using preorder traversal."""

        def preorder(node):
            if not node:
                # Append null for missing nodes
                result.append("null")
                return
            # Append the value of the current node
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        result = []
        preorder(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree using preorder traversal."""

        def build_tree():
            nonlocal index
            if values[index] == "null":
                index += 1
                return None

            # Create the current node and recurse
            node = TreeNode(int(values[index]))
            index += 1
            node.left = build_tree()
            node.right = build_tree()
            return node

        if not data:
            return None

        values = data.split(",")
        index = 0
        return build_tree()
