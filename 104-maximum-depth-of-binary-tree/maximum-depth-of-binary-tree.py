# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        

        def height(node):
            if not node:
                return 0

            left = height(node.left) if node.left else 0
            right = height(node.right) if node.right else 0

            return 1+ max(left, right)
        return height(root)
