# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return root
        
        self.arr = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.arr.append(node.val)
            inorder(node.right)
        inorder(root)
        
        n = len(self.arr)
        for i in range(n):
            for j in range(i):
                if self.arr[i] + self.arr[j] == k:
                    return True
        return False
            
            
            
        
            