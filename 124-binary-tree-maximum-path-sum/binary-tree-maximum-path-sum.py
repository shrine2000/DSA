# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        s = float("-inf")

        def max_path_sum(root):
            nonlocal s
            if not root:
                return 0

            l = max(0, max_path_sum(root.left))
            r = max(0, max_path_sum(root.right))

            s = max(s, l + r + root.val)

            return root.val + max(l, r)

        max_path_sum(root)
        return s
