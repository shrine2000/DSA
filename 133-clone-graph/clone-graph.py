"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, root: Optional["Node"]) -> Optional["Node"]:
        visited = {}

        def dfs(node):
            if not node:
                return None

            if node in visited:
                return visited[node]

            new_node = Node(val=node.val)
            visited[node] = new_node
            for ngbr in node.neighbors:
                new_node.neighbors.append(dfs(ngbr))
            return new_node

        return dfs(root)
