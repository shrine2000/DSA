# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def checkPathSum(node, current_sum):
            if not node:
                return False

            current_sum += node.val

            if not node.left and not node.right:
                return current_sum == targetSum

            return checkPathSum(node.left, current_sum) or checkPathSum(node.right, current_sum)

        return checkPathSum(root, 0) if root else False
