**LCA (Lowest Common Ancestor)** in a binary tree refers to the deepest node that is an ancestor of both nodes you're searching for. In simpler terms, it's the lowest (or deepest) node that is common to both nodes in the tree.

For example, given a binary tree:

```
        1
       / \
      2   3
     / \
    4   5
```

If you're asked for the LCA of nodes 4 and 5, the answer is node 2, because it is the deepest node that is an ancestor of both nodes 4 and 5.

### How to Find the LCA:
1. **If the current node is `None`, return `None`.** This means we've hit the bottom of the tree.
2. **If the current node is one of the nodes we're looking for**, return this node because it could be part of the path to the LCA.
3. **Recursively search both left and right subtrees**. If both left and right subtrees return non-`None` values, it means one node was found in the left subtree and the other in the right subtree, and the current node is the LCA.
4. **If both left and right subtrees are `None`**, return `None` — meaning no LCA found on that path.
5. **If only one subtree returns a non-`None` node**, it means the LCA is in that subtree.

### Recursive Algorithm for Finding LCA:

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_LCA(root, n1, n2):
    # Base case: if root is None, or if we've found one of the nodes
    if root is None or root.value == n1 or root.value == n2:
        return root

    # Recurse for left and right subtrees
    left = find_LCA(root.left, n1, n2)
    right = find_LCA(root.right, n1, n2)

    # If both left and right are not None, current node is the LCA
    if left and right:
        return root

    # Otherwise, return the non-None child (if any)
    return left if left else right

# Example Usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

lca = find_LCA(root, 4, 5)
print(lca.value)  # Output will be 2 (the LCA of nodes 4 and 5)
```

### Explanation:
- **Base Case**: The function checks whether the current node (`root`) is `None` or matches either `n1` or `n2`. If it does, it returns the node. This is because a node is the LCA of itself.
- **Recurse Left and Right**: It recursively searches the left and right subtrees of the current node.
- **If both left and right are non-`None`**: This means that one node is found in the left subtree and the other in the right subtree. So, the current node is the LCA.
- **If only one child is non-`None`**: This means both nodes are either in the left subtree or the right subtree, so the function returns the non-`None` child.

### Time Complexity:
- **O(N)** where `N` is the number of nodes in the binary tree. In the worst case, we might need to visit all nodes in the tree.

### Space Complexity:
- **O(H)** where `H` is the height of the tree. This is due to the recursion stack. In the worst case, the height could be equal to the number of nodes in a skewed tree, so the space complexity can also be O(N).

