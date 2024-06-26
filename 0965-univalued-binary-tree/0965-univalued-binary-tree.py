# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def isSame(root, value):
            if not root:
                return True
            if root.val != value:
                return False

            return isSame(root.left, value) and isSame(root.right, value)

        return isSame(root, root.val) if root else False
