# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)  
            right = helper(node.right) 
            self.depth = max(self.depth, 1 + max(left, right))
            return 1 + max(left, right)
        helper(root)
        return self.depth
