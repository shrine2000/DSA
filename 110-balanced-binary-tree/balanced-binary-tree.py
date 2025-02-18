# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0

    def height(self, node):
        if not node: return 0

        left = self.height(node.left)
        right = self.height(node.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return - 1

        return max(left, right) + 1