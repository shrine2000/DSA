# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        
        def traverse(root):
            nonlocal freq
            if root:
                traverse(root.left)
                freq[root.val] += 1
                traverse(root.right)
                
        traverse(root)
        
        max_freq = max(freq.values(), default=0)
        
        mode = [k for k, v in freq.items() if v == max_freq]
        
        return mode
        
        