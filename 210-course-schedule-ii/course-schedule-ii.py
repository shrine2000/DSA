class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for ngbr in graph[node]:
                indegree[ngbr] -= 1
                if indegree[ngbr] == 0:
                    queue.append(ngbr)
        if len(order) == numCourses:
            return order
        return []
