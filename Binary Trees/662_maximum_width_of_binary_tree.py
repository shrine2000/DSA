# Definition for a binary tree TreeNode.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = deque([(root, 0)])

        while queue:
            level_length = len(queue)
            _, first_idx = queue[0]
            for i in range(level_length):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * idx))
                if node.right:
                    queue.append((node.right, 2 * idx + 1))
                if i == level_length - 1:
                    max_width = max(max_width, idx - first_idx + 1)

        return max_width


if __name__ == "__main__":
    # Construct the binary tree
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.right = TreeNode(2)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(7)

    sol = Solution()
    print("Maximum width of the binary tree:", sol.widthOfBinaryTree(root))
