from typing import List

class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        def has_cycle(node, parent, visited):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if has_cycle(neighbor, node, visited):
                        return True
                # If the neighbor is visited and not the parent of the current node,
                # then there is a cycle in the graph.
                elif neighbor != parent:
                    return True
            return False

        # Initialize all nodes as not visited.
        visited = [False] * V

        # Perform DFS for each node in the graph.
        for node in range(V):
            if not visited[node]:
                if has_cycle(node, -1, visited):
                    return True
        return False
	           


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends