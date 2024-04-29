class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        graph = defaultdict(list)
        queue = deque([(root, None)])

        while queue:
            node, parent = queue.popleft()
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)

                queue.append((node.left, node))
                queue.append((node.right, node))

        distances = {start: 0}
        queue = deque([start])

        while queue:
            current_node = queue.popleft()
            for neighbor in graph[current_node]:
                if neighbor not in distances:
                    distances[neighbor] = distances[current_node] + 1
                    queue.append(neighbor)

        return max(distances.values())
