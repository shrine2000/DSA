class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        adj: List[List[int]] = [[] for _ in range(len(coins))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)        
        dp = [[-1] * 14 for _ in range(n)]
        def dfs(node: int, parent: int, power: int) -> int:
            if power >= 14:
                return 0
            if dp[node][power] != -1:
                return dp[node][power]
            
            coins_at_node: int = coins[node]
            case1: int = (coins_at_node >> power) - k
            case2: int = coins_at_node >> (power + 1)
            
            for neighbor in adj[node]:
                if neighbor != parent:
                    case1 += dfs(neighbor, node, power)
                    case2 += dfs(neighbor, node, power + 1)
            
            result: int = max(case1, case2)
            dp[node][power] = result
            return result
        return dfs(0, -1, 0)
            