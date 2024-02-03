# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse(root, a):
            if root:
                if root.left == None and root.right == None:
                    a.append(root.val)
                    
                else:
                    traverse(root.left, a)
                    traverse(root.right, a)
                    
                return a
        a, b = [], []
        x = traverse(root1, a)
        y = traverse(root2, b)
        
        return x == y
        