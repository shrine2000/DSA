# User function Template for python3
"""
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

"""


class Solution:
    # Function to sort a linked list of 0s, 1s, and 2s.
    def segregate(self, head):
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        if not head or not head.next:
            return head

        # Count the number of occurrences of 0s, 1s, and 2s
        current = head
        zero_count = one_count = two_count = 0

        while current:
            if current.data == 0:
                zero_count += 1
            elif current.data == 1:
                one_count += 1
            else:
                two_count += 1

            current = current.next

        # Update the values in the linked list based on counts
        current = head

        while current:
            if zero_count > 0:
                current.data = 0
                zero_count -= 1
            elif one_count > 0:
                current.data = 1
                one_count -= 1
            else:
                current.data = 2
                two_count -= 1

            current = current.next

        return head


# {
# Driver Code Starts
# Initial Template for Python 3
# Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(" ")
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        printList(Solution().segregate(a.head))
# } Driver Code Ends
