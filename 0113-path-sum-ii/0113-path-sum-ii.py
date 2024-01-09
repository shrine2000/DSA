# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths  = []
        
        def find_paths(node, target, path):
            if node is None:
                return
            path.append(node.val)
            
            if not node.left and not node.right and target == node.val:
                paths.append(list(path))
                
            find_paths(node.left, target - node.val, path)
            find_paths(node.right, target - node.val, path)
            
            
            path.pop()
            
        find_paths(root, targetSum, [])
        return paths
        
        