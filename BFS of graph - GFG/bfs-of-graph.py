# User function Template for python3

from typing import List
from queue import Queue


class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        ans = []
        vis = [False] * V

        q = Queue(maxsize=0)
        q.put(0)

        vis[0] = True

        while q.empty() == False:
            v = q.get()
            ans.append(v)

            for i in adj[v]:
                if vis[i] == False:
                    vis[i] = True
                    q.put(i)

        return ans


# {
# Driver Code Starts


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()


# } Driver Code Ends
