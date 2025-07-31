from typing import Optional, Dict

# https://www.enjoyalgorithms.com/blog/implement-least-recently-used-cache


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next: Optional["Node"] = None
        self.prev: Optional["Node"] = None


class LRUCache:
    """
    implemented using hashmap + doubly linked list (DLL)
    head represents Least Recently Used
    tail represents Most Recently Used

    def get() -> corresponding node is moved to MRU
    def put() -> updates an existing entry (moving it to MRU) or adds a new entry

    if cache exceeds, LRU node (ie one next to head) is removed

    """

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: dict[int, Node] = {}  # hold keys and their corresponding nodes
        self.head: Node = Node(0, 0)  # dummy head
        self.tail: Node = Node(0, 0)  # dummy tail

        # initialize doubly linked list
        self.head.next = (
            self.tail
        )  # prev of dummy head points to NULL and next point to dummy tail
        self.tail.prev = (
            self.head
        )  # prev of dummy tail points to head, next point to NULL

    def _remove(self, node: Node):
        """remove node from dll"""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_tail(self, node: Node):
        """add node right before the tail (most recently used)"""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # move the accessed node to tail (MRU)
            self._add_to_tail(node)
            return node.value
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self._remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            # remove the least recently used node which is right after the head
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
        # add new node or update the existing node
        new_node = Node(key, value)
        self._add_to_tail(new_node)
        self.cache[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
