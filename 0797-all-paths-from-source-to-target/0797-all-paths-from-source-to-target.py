class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        
        def dfs(node, path):
            if node == n - 1:
                paths.append(path[:])
                return 
            
            for next_node in graph[node]:
                path.append(next_node)
                dfs(next_node, path)
                path.pop()
            
        dfs(0, [0])
        return paths