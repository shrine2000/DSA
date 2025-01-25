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

        cloned_node = {}
        cloned_node[node] = Node(val=node.val)
        queue = deque([node])

        while queue:
            current = queue.popleft()
            for ngbr in current.neighbors:
                if ngbr not in cloned_node:
                    cloned_node[ngbr] = Node(ngbr.val)
                    queue.append(ngbr)
                cloned_node[current].neighbors.append(cloned_node[ngbr])

        return cloned_node[node]
