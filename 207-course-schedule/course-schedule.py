class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        visited = [False] * numCourses
        on_path = [False] * numCourses

        def has_cycle(node) -> bool:
            if on_path[node]:
                return True
            if visited[node]:
                return False
            
            visited[node] =True
            on_path[node] = True

            for ngbr in graph[node]:
                if has_cycle(ngbr):
                    return True
            on_path[node] = False
            return False
        
        for course in range(numCourses):
            if not visited[course] and has_cycle(course):
                return False
        return True

