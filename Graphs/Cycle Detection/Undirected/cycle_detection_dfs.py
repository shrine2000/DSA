def detect_cycle(graph) -> bool:
    visited = set()

    def dfs(node, parent) -> bool:
        visited.add(node)
        for ngbr in graph[node]:
            if ngbr not in visited:
                if dfs(node=ngbr, parent=node):
                    return True
            elif ngbr != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


if __name__ == "__main__":
    graph_with_cycle = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3]}
    graph_without_cycle = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3]}

    print(detect_cycle(graph_with_cycle))  # True
    print(detect_cycle(graph_without_cycle))  # False
