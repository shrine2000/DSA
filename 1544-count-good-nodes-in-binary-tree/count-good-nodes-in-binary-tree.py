# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, current_max):
            count = 0
            if not node:
                return 0
            
            if node.val >= current_max:
                count += 1
                current_max = node.val
            
            count += dfs(node.left, current_max)
            count += dfs(node.right, current_max)
            return count
        return dfs(root, float('-inf'))

            

