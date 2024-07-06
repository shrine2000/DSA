from typing import List


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def verticalTraversalDfs(root: Node) -> List[List[int]]:
        # Traverse the tree and store each node's value along with its position (level and vertical distance from root)
        def dfs(node, level, vertical_distance):
            if not node:
                return
            nodes.append((level, vertical_distance, node.val))
            dfs(
                node.left, level + 1, vertical_distance - 1
            )  # Traverse left with increased level and decreased vertical distance
            dfs(
                node.right, level + 1, vertical_distance + 1
            )  # Traverse right with increased level and increased vertical distance

        nodes = []
        dfs(root, 0, 0)

        # Sort the nodes firstly by vertical distance, then by level, and finally by the node's value
        nodes.sort(key=lambda x: (x[1], x[0], x[2]))

        # Group the nodes by their vertical distance
        result = []
        prev_vertical_distance = float(
            "-inf"
        )  # Initialize with negative infinity (to ensure the first vertical distance is different)

        for level, vertical_distance, value in nodes:
            if prev_vertical_distance != vertical_distance:
                # Start a new grouping when the vertical distance changes
                result.append([])
                prev_vertical_distance = vertical_distance
            result[-1].append(
                value
            )  # Add the current node's value to the current vertical grouping

        return result

    @staticmethod
    def verticalTraversal(root: Node) -> List[List[int]]:
        if not root:
            return []

        column_table = defaultdict(list)
        min_column = max_column = 0

        queue = deque([(root, 0, 0)])

        while queue:
            node, row, column = queue.popleft()
            if node:
                column_table[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                queue.append((node.left, row + 1, column - 1))
                queue.append((node.right, row + 1, column + 1))

        result = []
        for column in range(min_column, max_column + 1):
            result.append([val for row, val in sorted(column_table[column])])

        return result


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(10)
    root.left.left.right = Node(5)
    root.left.left.right.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(10)
    root.right.left = Node(9)

    print(Solution.verticalTraversalDfs(root))
