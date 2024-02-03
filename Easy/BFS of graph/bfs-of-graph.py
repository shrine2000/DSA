# User function Template for python3

from typing import List
from queue import Queue


class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        s = 0
        visited = [False] * V
        queue = Queue()
        queue.put(s)
        visited[s] = True
        result = []

        while not queue.empty():
            s = queue.get()
            result.append(s)

            for i in adj[s]:
                if not visited[i]:
                    queue.put(i)
                    visited[i] = True

        return result


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
