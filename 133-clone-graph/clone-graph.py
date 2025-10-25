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
        visited = {}
        def dfs(node):
            if not node:
                return

            if node in visited:
                return visited[node]
            
            root = Node(val=node.val)
            visited[node] = root

            root.neighbors = [dfs(ngbr) for ngbr in node.neighbors]
            return root
        return dfs(node)