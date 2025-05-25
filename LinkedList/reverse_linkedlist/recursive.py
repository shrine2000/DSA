class LinkedList:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverseLinkedListIterative(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def reverseLinkedListRecursive(head):
    if not head or not head.next:
        return head
    new_head = reverseLinkedListRecursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("\n")


if __name__ == "__main__":
    head = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(6)))))
    print("LIST: \n")
    printLinkedList(head)

    head = reverseLinkedListRecursive(head)
    print("Reversed: \n")
    printLinkedList(head)
