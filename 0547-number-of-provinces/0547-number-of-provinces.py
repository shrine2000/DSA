from typing import List

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(M, visited, i):
            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(M, visited, j)
        
        n = len(M)
        visited = [0] * n  
        circles = 0
        
        for i in range(n):
            if visited[i] == 0:  
                dfs(M, visited, i)
                circles += 1
                
        return circles
