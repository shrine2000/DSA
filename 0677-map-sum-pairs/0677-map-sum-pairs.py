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

        stack = [node]
        total = 0
        while stack:
            current_node = stack.pop()
            total += current_node.value
            stack.extend(current_node.children.values())
        return total


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
