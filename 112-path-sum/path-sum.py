# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, curr):
            if not node.left and not node.right:
                return curr == targetSum

            left = dfs(node.left, curr + node.left.val) if node.left else False
            right = dfs(node.right, curr + node.right.val) if node.right else False

            return left or right

        return dfs(root, root.val)
