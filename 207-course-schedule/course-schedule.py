class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        completed = 0

        while q:
            node = q.popleft()
            completed += 1

            for ngbr in graph[node]:
                indegree[ngbr] -= 1
                if indegree[ngbr] == 0:
                    q.append(ngbr)
        return completed == numCourses

