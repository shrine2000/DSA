class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_path_sum(node):
            nonlocal max_sum

            if not node:
                return 0

            left_sum = max(0, max_path_sum(node.left))
            right_sum = max(0, max_path_sum(node.right))

            max_sum = max(max_sum, node.val + left_sum + right_sum)

            return node.val + max(left_sum, right_sum)

        max_sum = float("-inf")

        max_path_sum(root)

        return max_sum
