class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.helper(root) != -1

    def helper(self, node: TreeNode) -> int:
        if node is None:
            return 0
        left_height = self.helper(node.left)
        right_height = self.helper(node.right)
        if (
            left_height == -1
            or right_height == -1
            or abs(left_height - right_height) > 1
        ):
            return -1
        return max(left_height, right_height) + 1


if __name__ == "__main__":
    # Construct the binary tree
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.right = TreeNode(2)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(7)

    solution = Solution()
    result = solution.isBalanced(root)
    print(f"Is the binary tree balanced? {result}")
