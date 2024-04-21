# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        s1, s2 = [], []
        
        while root1 or root2 or s1 or s2:
            while root1:
                s1.append(root1)
                root1 = root1.left
            while root2:
                s2.append(root2)
                root2 = root2.left
            if not s2 or (s1 and s1[-1].val <= s2[-1].val):
                node = s1.pop()
                res.append(node.val)
                root1 = node.right
            else:
                node = s2.pop()
                res.append(node.val)
                root2 = node.right
                
        return res