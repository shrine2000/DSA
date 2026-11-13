# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.count = 0
        self.answer = 0

        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.answer = node.val
            inorder(node.right)
        inorder(root)
        return self.answer