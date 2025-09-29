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

        def dfs(graph):
            if not graph:
                return None
                
            if graph in visited:
                return visited[graph]
            current = Node(val=graph.val)
            visited[graph] = current
            for ngbr in graph.neighbors:
                current.neighbors.append(dfs(ngbr))
            return current
        
        return dfs(node)

