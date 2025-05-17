class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache ={}
        self.capacity=capacity
        self.tail=Node(0, 0)
        self.head=Node(0, 0)

        self.head.next=self.tail
        self.tail.prev=self.head

    def _remove(self,node):
        _prev=node.prev
        _next=node.next
        _prev.next=_next
        _next.prev=_prev
  
    def _add_to_tail(self,node):
        tail_prev=self.tail.prev
        tail_prev.next=node
        node.prev=tail_prev
        node.next=self.tail
        self.tail.prev=node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            self._add_to_tail(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        elif len(self.cache) >= self.capacity:
            lru=self.head.next
            self._remove(lru)
            del self.cache[lru.key]
        new_node=Node(key,value)
        self._add_to_tail(new_node)
        self.cache[key]=new_node

        

 
