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
        if not node:
            return None

        visited = {}

        queue = deque([node])

        cloned_node = Node(node.val)
        visited[node] = cloned_node

        while queue:
            cn = queue.popleft()

            for neighbor in cn.neighbors:
                if neighbor not in visited:
                    cngbr = Node(neighbor.val)
                    visited[neighbor] = cngbr
                    queue.append(neighbor)

                visited[cn].neighbors.append(visited[neighbor])

        return visited[node]
