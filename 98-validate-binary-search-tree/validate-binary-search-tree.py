# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        order = []
        def in_order(node):
            if not node:
                return 
            in_order(node.left)
            order.append(node.val)
            in_order(node.right)
        in_order(root)
        
        for i in range(len(order)-1):
            if order[i] >= order[i+1]:
                return False
            
        return True
            