class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
        

        def has_cycle(start):
            visited = set()
            stack = [start]
            while stack:
                node = stack.pop()
                for ngbr in graph[node]:
                    if ngbr == start:
                        return True
                    if ngbr not in visited:
                        visited.add(ngbr)
                        stack.append(ngbr)
            return False
        
        for i in range(numCourses):
            if has_cycle(i):
                return False
        return True