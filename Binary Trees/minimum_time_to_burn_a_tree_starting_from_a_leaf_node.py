class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


from collections import deque


def min_time_to_burn_tree_optimized(root, leaf):
    def find_parent_mapping(node, parent, parent_map):
        if not node:
            return
        parent_map[node] = parent
        find_parent_mapping(node.left, node, parent_map)
        find_parent_mapping(node.right, node, parent_map)

    # Create a map to track the parent of each node
    parent_map = {}
    find_parent_mapping(root, None, parent_map)

    # BFS from the leaf node
    queue = deque([(leaf, 0)])
    visited = set()
    max_time = 0

    while queue:
        current_node, current_time = queue.popleft()
        if current_node in visited:
            continue

        # Mark the current node as visited
        visited.add(current_node)
        # Update the maximum time
        max_time = max(max_time, current_time)

        # Enqueue the left child if it exists and is not visited
        if current_node.left and current_node.left not in visited:
            queue.append((current_node.left, current_time + 1))
        # Enqueue the right child if it exists and is not visited
        if current_node.right and current_node.right not in visited:
            queue.append((current_node.right, current_time + 1))
        # Enqueue the parent node if it exists and is not visited
        parent_node = parent_map.get(current_node)
        if parent_node and parent_node not in visited:
            queue.append((parent_node, current_time + 1))

    return max_time


# Example Usage
# Constructing the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)

# Starting leaf node
leaf_node = root.left.left.left

# Calculating the minimum time to burn the tree starting from the leaf node
print(min_time_to_burn_tree_optimized(root, leaf_node))  # Output: 4
