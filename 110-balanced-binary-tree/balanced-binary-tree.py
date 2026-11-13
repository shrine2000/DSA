# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        # subtree
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)
            return 1 + max(left, right)
        
        l = height(root.left)
        r = height(root.right)
        if abs(r - l) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
