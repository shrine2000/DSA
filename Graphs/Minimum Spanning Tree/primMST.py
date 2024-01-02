from typing import List, Tuple, Optional


class PrimMST:
    def __init__(self, vertices: int):
        self.V: int = vertices  # Number of vertices
        self.graph: List[List[int]] = []  # Adjacency matrix to represent the graph

    def select_min_vertex(self, value: List[int], set_MST: List[bool]) -> Optional[int]:
        # Helper function to select the vertex with the minimum value that is not yet included in MST
        minimum: int = float("inf")
        vertex: Optional[int] = None
        for i in range(self.V):
            if not set_MST[i] and value[i] < minimum:
                vertex = i
                minimum = value[i]
        return vertex

    def find_MST(self) -> List[Tuple[int, int, int]]:
        parent: List[int] = [-1] * self.V  # Stores MST
        value: List[int] = [float("inf")] * self.V  # Used for edge relaxation
        set_MST: List[bool] = [False] * self.V  # TRUE->Vertex is included in MST

        # Assuming start point as Node-0
        parent[0] = -1  # Start node has no parent
        value[0] = 0  # Start node has value=0 to get picked first

        # Form MST with (V-1) edges
        for i in range(self.V - 1):
            # Select the best Vertex by applying the greedy method
            U: Optional[int] = self.select_min_vertex(value, set_MST)
            if U is None:
                break
            set_MST[U] = True  # Include new Vertex in MST

            # Relax adjacent vertices (not yet included in MST)
            for j in range(self.V):
                """
                3 constraints to relax:-
                    1. Edge is present from U to j.
                    2. Vertex j is not included in MST.
                    3. Edge weight is smaller than the current edge weight.
                """
                if (
                    self.graph[U][j] != 0
                    and not set_MST[j]
                    and self.graph[U][j] < value[j]
                ):
                    value[j] = self.graph[U][j]
                    parent[j] = U

        # Return the MST edges
        mst_edges: List[Tuple[int, int, int]] = []
        for i in range(1, self.V):
            mst_edges.append((parent[i], i, self.graph[parent[i]][i]))

        return mst_edges


if __name__ == "__main__":
    graph: List[List[int]] = [
        [0, 4, 6, 0, 0, 0],
        [4, 0, 6, 3, 4, 0],
        [6, 6, 0, 1, 8, 0],
        [0, 3, 1, 0, 2, 3],
        [0, 4, 8, 2, 0, 7],
        [0, 0, 0, 3, 7, 0],
    ]

    # Create an instance of PrimMST
    prim: PrimMST = PrimMST(len(graph))
    prim.graph = graph

    # Find the Minimum Spanning Tree (MST)
    result: List[Tuple[int, int, int]] = prim.find_MST()

    # Print MST edges
    print("Edges in the constructed MST:")
    for edge in result:
        print(f"U->V: {edge[0]}->{edge[1]}  wt = {edge[2]}")
