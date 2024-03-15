class Solution:
    def dfs(self, tree: List[List[int]], values: List[int], node: int, parent: int) -> (int, int):
        leftout = 0
        taken = 0
        
        for c in tree[node]:
            if c == parent:
                continue
            t, l = self.dfs(tree, values, c, node)
            taken += t
            leftout += l
        
        if leftout != 0:
            taken += max(leftout, values[node])
        
        leftout = min(leftout, values[node]) if leftout != 0 else values[node]
        
        return taken, leftout

    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        tree = [[] for _ in range(len(values))]
        
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])
        
        return self.dfs(tree, values, 0, -1)[0]