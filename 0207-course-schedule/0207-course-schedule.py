class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        def has_cycle(course, visited, recursion_stack):
            visited[course] = True
            recursion_stack[course] = True

            for neighbor in graph[course]:
                if not visited[neighbor]:
                    if has_cycle(neighbor, visited, recursion_stack):
                        return True
                elif recursion_stack[neighbor]:
                    return True

            recursion_stack[course] = False
            return False

        visited = [False] * numCourses
        recursion_stack = [False] * numCourses

        for course in range(numCourses):
            if not visited[course]:
                if has_cycle(course, visited, recursion_stack):
                    return False

        return True
