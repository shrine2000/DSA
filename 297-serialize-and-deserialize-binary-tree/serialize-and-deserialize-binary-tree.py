# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)            
            else:
                result.append("")
        return ",".join(result)
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if values[i] != "":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            if values[i] != '':
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
                
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))