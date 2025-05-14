# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.left_sum, self.right_sum = 0, 0
        self.max_sum = -1000

        def helper(node):
            if not node:
                return 0
            left_sum = max(0, helper(node.left)) if node.left else 0
            right_sum = max(0, helper(node.right)) if node.right else 0
            self.max_sum = max(self.max_sum, left_sum + right_sum + node.val)
            return node.val + max(left_sum, right_sum)

        helper(root)
        return self.max_sum
