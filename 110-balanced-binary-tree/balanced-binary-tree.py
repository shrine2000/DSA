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

        left_sub = height(root.left)
        right_sub = height(root.right)

        if abs(left_sub - right_sub) > 1:
            return False

        return bool(self.isBalanced(root.left) and self.isBalanced(root.right))
