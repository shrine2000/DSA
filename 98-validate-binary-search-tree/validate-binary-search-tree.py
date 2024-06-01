class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(node: Optional[TreeNode], minVal: float, maxVal: float) -> bool:
            if not node:
                return True
            if not (minVal < node.val < maxVal):
                return False
            return isBST(node.left, minVal, node.val) and isBST(node.right, node.val, maxVal)
        return isBST(root, float("-inf"), float("inf"))