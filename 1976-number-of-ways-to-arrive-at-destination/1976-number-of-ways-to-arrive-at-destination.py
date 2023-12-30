from typing import List
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        graph = {i: [] for i in range(n)}
        for road in roads:
            u, v, time = road
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        min_time = [float('inf')] * n
        ways = [0] * n
        min_time[0] = 0
        ways[0] = 1
        
        min_heap = [(0, 0)]  # (time, node)
        
        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)
            if curr_time > min_time[curr_node]:
                continue
            
            for neighbor, time in graph[curr_node]:
                if curr_time + time < min_time[neighbor]:
                    min_time[neighbor] = curr_time + time
                    ways[neighbor] = ways[curr_node]
                    heapq.heappush(min_heap, (min_time[neighbor], neighbor))
                elif curr_time + time == min_time[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[curr_node]) % MOD
        
        return ways[n - 1] % MOD
