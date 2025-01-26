# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        def helper(node, prev):
            nonlocal count
            if node.left:
                helper(node.left, max(node.val, prev))
            if node.right:
                helper(node.right, max(node.val, prev))
            if node.val >= prev:
                count += 1
                
        helper(root, root.val)
        return count

        

