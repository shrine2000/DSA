# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        result = []
        
        result.append(root.val)
        
        left_subtree = self.preorderTraversal(root.left)
        result.extend(left_subtree)
        
        right_subtree = self.preorderTraversal(root.right)
        result.extend(right_subtree)
        
        return result
        