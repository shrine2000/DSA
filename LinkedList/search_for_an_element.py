class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, target):
        current = self.head

        while current:
            if current.data == target:
                return True

            current = current.next

        return False


linked_list = LinkedList()
linked_list.head = Node(1)
second_node = Node(2)
thrid_node = Node(3)
linked_list.head.next = second_node
second_node.next = thrid_node


target = 2

if linked_list.search(target=target):
    print("Element found")
else:
    print("Not found")
