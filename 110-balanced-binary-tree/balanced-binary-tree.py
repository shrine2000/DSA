# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            return 1 + max(left, right)

        if not root:
            return True

        l = height(root.left)
        r = height(root.right)
        if abs(l - r) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
