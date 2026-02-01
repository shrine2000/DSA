# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        def dfs(node):
            if not node:
                return "#"
            return str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)

        return dfs(root)

    def deserialize(self, data):
        def dfs(nodes):
            val = next(nodes)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs(nodes)
            node.right = dfs(nodes)
            return node

        nodes = iter(data.split(","))
        return dfs(nodes)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
