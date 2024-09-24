class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        
        for _, to in edges:
            in_degree[to] += 1
            
        result = [node for node in range(n) if in_degree[node] == 0]
        
        return result