# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, curr_max):
            if not node:
                return 0

            nonlocal count

            if node.val >= curr_max:
                count += 1
            curr_max = max(node.val, curr_max)
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)
            return count

        dfs(root, float("-inf"))
        return count
