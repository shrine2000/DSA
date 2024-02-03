# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def find_longest_path(node):
            nonlocal max_path
            if not node:
                return 0
            
            l = find_longest_path(node.left)
            r = find_longest_path(node.right)
            
            lp = l + 1 if node.left and node.left.val == node.val else 0
            rp = r + 1 if node.right and node.right.val == node.val else 0
            
            max_path = max(max_path, lp + rp)
            
            return max(lp, rp)
            
        max_path = 0
        
        find_longest_path(root)
        return max_path
        