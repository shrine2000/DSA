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

        visited = {}

        def dfs(value):
            if value is None:
                return None
            if value in visited:
                return visited[value]

            new_node = Node(val=value.val)
            visited[value] = new_node
            for ngbr in value.neighbors:
                new_node.neighbors.append(dfs(ngbr))
            visited[value] = new_node
            return new_node

        return dfs(node)
