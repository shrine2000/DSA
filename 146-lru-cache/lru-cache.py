class Node:
    def __init__(self, key=None, val=None):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val


class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(0)
        self.tail = Node(0)
        self.capacity = capacity
        self.cache = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        prev, next = self.head, self.head.next
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
