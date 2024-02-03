"""
1245. Tree Diameter
Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

https://leetcode.ca/all/1245.html
https://github.com/doocs/leetcode/blob/main/solution/1200-1299/1245.Tree%20Diameter/README_EN.md
"""

from typing import List
from collections import defaultdict


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # Helper function to perform DFS traversal to find the diameter
        def dfs(node, distance):
            nonlocal max_distance, visited, adjacency, next_node

            # Mark the node as visited
            if visited[node]:
                return
            visited[node] = True

            # Explore adjacent nodes and update the distance
            for adjacent_node in adjacency[node]:
                dfs(adjacent_node, distance + 1)

            # Update the maximum distance encountered
            if max_distance < distance:
                max_distance = distance
                next_node = node

        # Creating an adjacency list representation of the tree
        adjacency = defaultdict(set)
        visited = [False] * (len(edges) + 1)
        for u, v in edges:
            adjacency[u].add(v)
            adjacency[v].add(u)

        # Initialize variables to track maximum distance and next node
        max_distance = 0
        next_node = 0

        # Perform DFS from the first node and find the furthest node
        dfs(edges[0][0], 0)

        # Reset visited list and perform DFS from the furthest node to find diameter
        visited = [False] * (len(edges) + 1)
        dfs(next_node, 0)

        return max_distance
