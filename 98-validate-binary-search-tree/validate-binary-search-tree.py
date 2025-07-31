# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(node, low, high):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            

            left_tree = dfs(node.left, low, node.val)

            right_tree = dfs(node.right, node.val, high)


            return bool(left_tree and right_tree)
        
        return dfs(root, float('-inf'), float('inf'))