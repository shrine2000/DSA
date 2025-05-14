from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Initialize a dummy node to start the result list
        dummy = ListNode()
        temp = dummy
        carry = 0

        # Loop until both lists are exhausted and carry is zero
        while (l1 is not None or l2 is not None) or carry:
            sum_value = carry  # Start with any carry from previous addition

            # Add l1's value if it exists
            if l1 is not None:
                sum_value += l1.val
                l1 = l1.next

            # Add l2's value if it exists
            if l2 is not None:
                sum_value += l2.val
                l2 = l2.next

            # Calculate carry and the new node value
            carry = sum_value // 10
            temp.next = ListNode(sum_value % 10)
            temp = temp.next  # Move to the next node

        # Return the next of dummy (first actual node)
        return dummy.next


def print_linked_list(head: ListNode) -> None:
    """Helper function to print a linked list"""
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))


def create_linked_list(values: list) -> ListNode:
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


if __name__ == "__main__":
    # Test Case 1: Equal Length, No Carry
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    print("Test Case 1 (Equal Length, No Carry):")
    print_linked_list(result)  # Expected: 7 -> 0 -> 8
    print("\n" + "-" * 50)

    # Test Case 2: Different Length, No Carry
    l1 = create_linked_list([9])
    l2 = create_linked_list([1, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print("Test Case 2 (Different Length, No Carry):")
    print_linked_list(result)  # Expected: 0 -> 0 -> 0 -> 1
    print("\n" + "-" * 50)

    # Test Case 3: Different Length, With Carry
    l1 = create_linked_list([9, 9])
    l2 = create_linked_list([1])
    result = solution.addTwoNumbers(l1, l2)
    print("Test Case 3 (Different Length, With Carry):")
    print_linked_list(result)  # Expected: 0 -> 0 -> 1
    print("\n" + "-" * 50)

    # Test Case 4: One List is Empty
    l1 = create_linked_list([])
    l2 = create_linked_list([1, 2, 3])
    result = solution.addTwoNumbers(l1, l2)
    print("Test Case 4 (One List is Empty):")
    print_linked_list(result)  # Expected: 1 -> 2 -> 3
    print("\n" + "-" * 50)

    # Test Case 5: Both Lists are Empty
    l1 = create_linked_list([])
    l2 = create_linked_list([])
    result = solution.addTwoNumbers(l1, l2)
    print("Test Case 5 (Both Lists are Empty):")
    print_linked_list(result)  # Expected: (No Output)
    print("\n" + "-" * 50)

    # Test Case 6: Large Numbers
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print("Test Case 6 (Large Numbers):")
    print_linked_list(result)  # Expected: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1
    print("\n" + "-" * 50)
