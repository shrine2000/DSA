class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def lca(self, root, p, q):
        if not root or root == p or root == q:
            return root
        l = self.lca(root.left, p, q)
        r = self.lca(root.right, p, q)

        if l and r:
            return root

        return l or r


if __name__ == "__main__":
    root = TreeNode(val=3)
    root.left = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    root.right = TreeNode(1, TreeNode(0), TreeNode(8))

    p = root.left
    q = root.right

    lcs_node = root.lca(root, p, q)
    print("LCA: ", lcs_node.val)
