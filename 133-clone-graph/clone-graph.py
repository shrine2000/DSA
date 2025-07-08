"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node or not node.val:
            return None
        visited = {}

        def dfs(current):
            if current in visited:
                return visited[current]
            clone = Node(current.val)
            visited[current] = clone
            for ngbr in current.neighbors:
                clone.neighbors.append(dfs(ngbr))
            return clone

        return dfs(node)
