# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        column_table = defaultdict(list)
        min_col = max_col = 0
        queue = deque([(root, 0, 0)])
        while queue:
            node, row, column = queue.popleft()
            if node:
                column_table[column].append((row, node.val))
                min_col = min(min_col, column)
                max_col = max(max_col, column)
                queue.append((node.left, row + 1, column - 1))
                queue.append((node.right, row + 1, column + 1))
        result = []
        for col in range(min_col, max_col + 1):
            result.append([v for r, v in sorted(column_table[col])])
        return result
