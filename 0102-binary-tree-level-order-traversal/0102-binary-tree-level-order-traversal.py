# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            lv = []
            ls = len(queue)
            
            for _ in range(ls):
                cn = queue.pop(0)
                lv.append(cn.val)
                
                if cn.left:
                    queue.append(cn.left)
                if cn.right:
                    queue.append(cn.right)
                    
            result.append(lv)
            
        return result