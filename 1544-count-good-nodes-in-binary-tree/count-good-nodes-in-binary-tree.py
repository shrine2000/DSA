# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(root, check):
            if root.val >= check:
                self.good += 1
            if root.left:
                dfs(root.left, max(root.val, check))
            if root.right:
                dfs(root.right, max(root.val, check))

        dfs(root, root.val)
        return self.good

if __name__ =="__main__":
    # Tree structure:
    #     3
    #    / \
    #   1   4
    #  /   / \
    # 3   1   5

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    solution = Solution()
    print(solution.goodNodes(root))  # Expected output: 4

    # Tree structure:
    #     3
    #    /
    #   3
    #  / \
    # 4   2

    root = TreeNode(3)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(2)

    solution = Solution()
    print(solution.goodNodes(root))  # Expected output: 3