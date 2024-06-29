# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://www.youtube.com/watch?v=4fiDs7CCxkc&t=134s
class Solution:
    def __init__(self):
        self.max_val = 0

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def post_order(node):
            if not node:
                return True, 0, float("inf"), float("-inf")

            left_is_bst, left_sum, left_min, left_max = post_order(node.left)
            right_is_bst, right_sum, right_min, right_max = post_order(node.right)

            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                curr_sum = left_sum + node.val + right_sum
                self.max_val = max(self.max_val, curr_sum)
                return True, curr_sum, min(left_min, node.val), max(right_max, node.val)
            else:
                return False, 0, 0, 0

        post_order(root)
        return self.max_val
