class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root, prev):
            if root is None:
                return True

            if not traverse(root.left, prev):
                return False

            if root.val <= prev[0]:
                return False

            prev[0] = root.val

            return traverse(root.right, prev)

        prev = [float("-inf")]

        return traverse(root, prev)
