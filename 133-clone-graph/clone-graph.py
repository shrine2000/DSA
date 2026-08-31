"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def dfs(root):
            if root in visited:
                return visited[root]

            copy = Node(root.val)
            visited[root] = copy

            for nei in root.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)