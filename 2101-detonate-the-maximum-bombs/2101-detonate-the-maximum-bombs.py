from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs):
        def dfs(node):
            nonlocal max_bombs
            visited.add(node)
            max_bombs += 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    dist = ((bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2)**0.5
                    if dist <= bombs[i][2]:
                        graph[i].append(j)

        max_detonated = 0


        for i in range(len(bombs)):
            visited = set()
            max_bombs = 0
            dfs(i)
            max_detonated = max(max_detonated, max_bombs)

        return max_detonated