class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = [i for i in range(numCourses) if indegree[i] == 0]
        order = []

        while queue:
            course = queue.pop(0)
            order.append(course)
            for ngbr in graph[course]:
                indegree[ngbr] -= 1
                if indegree[ngbr] == 0:
                    queue.append(ngbr)

        if len(order) != numCourses:
            return []

        return order
