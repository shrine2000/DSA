class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def delete_by_key(self, key):
        if self.head is not None and self.head.data == key:
            self.head = self.head.next
            return

        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_node.data == key:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


my_list = LinkedList()

# Add nodes to the linked list
my_list.head = Node(1)
second_node = Node(2)
third_node = Node(3)
my_list.head.next = second_node
second_node.next = third_node

# Display the initial linked list
print("Initial Linked List:")
my_list.display()

# Delete a node by key
my_list.delete_by_key(2)

# Display the modified linked list
print("Modified Linked List:")
my_list.display()
