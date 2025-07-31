# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return []

            return inorder(node.left) + [node.val] + inorder(node.right)

        res = inorder(root)
        return res[k - 1] if k <= len(res) else -1
