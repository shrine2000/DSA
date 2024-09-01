# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        
        queue = deque([(root, 1)])
        max_sum = float('-inf')
        max_level= 0
        while queue:
            level_sum = 0
            level_length = len(queue)
            current_level = queue[0][1]
            for i in range(level_length):
                node, idx = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append((node.left, idx + 1))
                if node.right:
                    queue.append((node.right, idx + 1))
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
        return max_level
    
                
            
            