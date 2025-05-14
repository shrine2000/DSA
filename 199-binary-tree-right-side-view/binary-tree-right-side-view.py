# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            level_range = len(queue)
            for i in range(level_range):
                current_level = queue.pop(0)
                if i == level_range - 1:
                    res.append(current_level.val)
                if current_level.left:
                    queue.append(current_level.left)
                if current_level.right:
                    queue.append(current_level.right)
        return res
