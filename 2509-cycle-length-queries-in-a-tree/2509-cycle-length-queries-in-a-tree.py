from typing import List


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Define a method to find the lowest common ancestor (LCA)
        def find_LCA(a, b):
            while a != b:
                if a > b:
                    a //= 2
                else:
                    b //= 2
            return a

        # Define a method to calculate the depth of a node
        def calculate_depth(node):
            depth = 0
            while node > 1:
                node //= 2
                depth += 1
            return depth

        def find_distance(a, b):
            lca = find_LCA(a, b)
            return calculate_depth(a) + calculate_depth(b) - 2 * calculate_depth(lca)

        def cycle_length(n, queries):
            result = []
            for query in queries:
                a, b = query
                distance = find_distance(a, b)
                result.append(
                    distance + 1
                )  # Adding 1 to the distance to account for the edge
            return result

        return cycle_length(n, queries)
