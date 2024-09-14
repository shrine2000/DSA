# User function Template for python3


class Solution:
    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        # code here
        import heapq

        visited = [False] * V

        pq = []

        heapq.heappush(pq, (0, 0))
        wgt = 0

        while pq:
            w, v = heapq.heappop(pq)

            if not visited[v]:
                visited[v] = True
                wgt += w

                for ngbr, ewgt in adj[v]:
                    if not visited[ngbr]:
                        heapq.heappush(pq, (ewgt, ngbr))

        return wgt


# {
# Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

if __name__ == "__main__":
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        ob = Solution()

        print(ob.spanningTree(V, adj))
# } Driver Code Ends
