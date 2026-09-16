# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left) + 1 if node.left else 0
            right = dfs(node.right) + 1 if node.right else 0

            self.dia = max(self.dia, left + right)
            return  max(left, right)
        dfs(root)
        return self.dia