class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node(value={self.value}, next={self.next})"

    @staticmethod
    def print_list_from(head):
        current = head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()
