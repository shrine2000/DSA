class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0
        
        
class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for k in key:
            if not k in node.children:
                node.children[k] = TrieNode()
            node = node.children[k]
        node.value = val
        

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return self._dfs(node)
    
    def _dfs(self, node):
        total = node.value
        for child in node.children.values():
            total += self._dfs(child)
        return total
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)