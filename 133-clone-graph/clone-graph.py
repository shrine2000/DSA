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
        visit = {}

        def dfs(root):
            if not root:
                return None
            if root in visit:
                return visit[root]
            clone = Node(root.val)
            visit[root] = clone
            for ngbr in root.neighbors:
                clone.neighbors.append(dfs(ngbr))
            return clone

        return dfs(node)
