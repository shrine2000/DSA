# User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None


class Solution:
    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):
        # code here

        if not root:
            return []

        queue = deque([(root, 0)])
        level_map = defaultdict(list)
        while queue:
            node, level = queue.popleft()
            level_map.get(level)
            level_map[level] = node.data
            if node.left:
                queue.append([node.left, level - 1])
            if node.right:
                queue.append([node.right, level + 1])

        return [v for k, v in sorted(hashmap.items())]


# {
# Driver Code Starts
# Initial Template for Python 3

from collections import deque, defaultdict


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree


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

    # Creating a Solution object
    solution = Solution()

    # Get the Bottom View traversal
    bottomView = solution.topView(root)


# } Driver Code Ends
