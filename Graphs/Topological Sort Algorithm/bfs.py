from collections import defaultdict, deque


def topo_sort(vertices, edges):
    in_degree = {v: 0 for v in vertices}
    adj_list = defaultdict(list)

    for edge in edges:
        from_vertex, to_vertex = edge
        in_degree[to_vertex] += 1
        adj_list[from_vertex].append(to_vertex)

    queue = deque([v for v in vertices if in_degree[v] == 0])
    topo_order = []

    while queue:
        current_vertex = queue.popleft()
        topo_order.append(current_vertex)

        for neighbor in adj_list[current_vertex]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != len(vertices):
        return None
    else:
        return topo_order


if __name__ == "__main__":
    vertices = [0, 1, 2, 3, 4]
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]

    result = topo_sort(vertices, edges)
    if result is None:
        print("The graph contains a cycle or unreachable vertices.")
    else:
        print("Topological order:", result)
