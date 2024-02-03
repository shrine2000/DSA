# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0

            l = height(node.left)
            r = height(node.right)
            return max(l, r) + 1

        def diameter(node):
            if not node:
                return 0
            l = diameter(node.left)
            r = diameter(node.right)
            t = height(node.left) + height(node.right)
            return max(l, r, t)

        return diameter(root)
