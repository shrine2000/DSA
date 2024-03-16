from typing import List, Set
from collections import defaultdict

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        def dfs(node, parent):
            leftout, taken = 0, 0
            for child in g[node]:
                if child != parent:
                    t, l = dfs(child, node)
                    taken += t
                    leftout += l
            taken += max(leftout, values[node]) if leftout != 0 else 0
            leftout = min(leftout, values[node]) if leftout != 0 else values[node]
            return taken, leftout

        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        
        return dfs(0, -1)[0]