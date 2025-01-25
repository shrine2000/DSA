from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.max_len = max(self.max_len, left + right)
            return max(left, right) + 1

        depth(root)
        return self.max_len


# Time Complexity:
# The time complexity remains O(N), where N is the number of nodes in the tree, because each node is visited once.
# Space Complexity:
# The space complexity is still O(H), where H is the height of the tree, due to the recursion stack.

if __name__ == "__main__":
    # Test case 1: A simple tree with only a single node
    root1 = TreeNode(1)
    # The tree is just one node, so diameter is 0 (no edges).
    assert Solution().diameterOfBinaryTree(root1) == 0

    # Test case 2: A tree with two nodes (one root and one child)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    # The tree has one edge (root to child), so the diameter is 1.
    assert Solution().diameterOfBinaryTree(root2) == 1

    # Test case 3: A full binary tree with 3 levels
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    root3.left.right = TreeNode(5)
    root3.right.left = TreeNode(6)
    root3.right.right = TreeNode(7)
    # The longest path is from node 4 to node 7, which has a length of 4 edges.
    assert Solution().diameterOfBinaryTree(root3) == 4

    # Test case 4: A skewed tree (like a linked list)
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    root4.left.left.left = TreeNode(4)
    # The longest path is from node 4 to node 1, which has a length of 3 edges.
    assert Solution().diameterOfBinaryTree(root4) == 3

    # Test case 5: An empty tree
    root5 = None
    # The tree is empty, so the diameter is 0.
    assert Solution().diameterOfBinaryTree(root5) == 0

    # Test case 6: A more complex tree
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.right = TreeNode(3)
    root6.left.left = TreeNode(4)
    root6.left.left.left = TreeNode(5)
    root6.right.left = TreeNode(6)
    assert Solution().diameterOfBinaryTree(root6) == 5

    print("All test cases passed!")
