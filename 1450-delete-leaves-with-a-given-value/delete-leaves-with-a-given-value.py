# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        if not root:
            return None

        def remove_leaf(node):
            if not node:
                return None
            node.left = remove_leaf(node.left)
            node.right = remove_leaf(node.right)

            if not node.left and not node.right and node.val == target:
                return None

            return node

        return remove_leaf(root)
