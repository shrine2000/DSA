from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case: root is None or root's value equals the search value
        if root     is None or root.val == val:
            return root

        # If the value to search for is less than root's value, search the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            # If the value to search for is greater than root's value, search the right subtree
            return self.searchBST(root.right, val)


# Helper function to build a binary search tree from a list of values
def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root


# Helper function to create a BST from a list of values
def build_bst_from_list(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    for val in vals[1:]:
        insert_into_bst(root, val)
    return root


def inorder_traversal(root):
    return (
        inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
        if root
        else []
    )


if __name__ == "__main__":
    vals = [4, 2, 7, 1, 3]
    bst_root = build_bst_from_list(vals)

    solution = Solution()

    # Search for value 2
    search_result = solution.searchBST(bst_root, 2)
    if search_result:
        print("Search result (inorder traversal):", inorder_traversal(search_result))
    else:
        print("Node not found")

    # Search for value 5
    search_result = solution.searchBST(bst_root, 5)
    if search_result:
        print("Search result (inorder traversal):", inorder_traversal(search_result))
    else:
        print("Node not found")
