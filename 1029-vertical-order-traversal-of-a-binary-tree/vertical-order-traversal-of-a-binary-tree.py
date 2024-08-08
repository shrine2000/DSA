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
        min_column = max_column = 0
        queue = deque([(root, 0, 0)])
        while queue:
            node, row, column = queue.popleft()
            if node:
                column_table[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                queue.append((node.left, row + 1, column - 1))
                queue.append((node.right, row + 1, column + 1))

        result = []
        for column in range(min_column, max_column + 1):
            result.append([val for row, val in sorted(column_table[column])])
        return result
