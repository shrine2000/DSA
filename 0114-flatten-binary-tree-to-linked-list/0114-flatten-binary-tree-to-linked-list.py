class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        def flatten_tree(node):
            if not node:
                return None

            left_last = flatten_tree(node.left)
            right_last = flatten_tree(node.right)

            right_subtree = node.right

            if node.left:
                node.right = node.left
                node.left = None

            if left_last:
                left_last.right = right_subtree

            return right_last if right_last else left_last if left_last else node

        flatten_tree(root)
