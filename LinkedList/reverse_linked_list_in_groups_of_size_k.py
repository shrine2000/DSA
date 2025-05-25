from typing import Optional
from LinkedList.node import Node
from LinkedList.reverse_linkedlist.recursive import reverseLinkedListIterative


def get_kth_node(start_node: Optional[Node], k: int) -> Optional[Node]:
    current = start_node
    steps_remaining = k - 1

    while current and steps_remaining > 0:
        current = current.next
        steps_remaining -= 1

    return current


def reverse_in_k_groups(head: Optional[Node], k: int) -> Optional[Node]:
    if k <= 1 or not head:
        return head

    dummy = Node(0)
    dummy.next = head
    prev_group_end = dummy

    while True:
        group_start = prev_group_end.next
        group_end = get_kth_node(group_start, k)

        if not group_end:
            break

        next_group_start = group_end.next
        group_end.next = None  # Temporarily break

        # Reverse current group
        reversed_head = reverseLinkedListIterative(group_start)

        # Reconnect with previous and next group
        prev_group_end.next = reversed_head
        group_start.next = next_group_start

        # Move to the end of the reversed group
        prev_group_end = group_start

    return dummy.next


def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 3
    head = build_linked_list(values)

    print("Original list:")
    print(head)

    new_head = reverse_in_k_groups(head, k)
    print(f"\nReversed in k={k} groups:")
    print(new_head)
