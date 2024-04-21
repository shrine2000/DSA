"""    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
"""


class Solution:
    # Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self, head, x):
        # code here

        newNode = Node(x)
        newNode.next = head
        return newNode

    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):
        # code here
        newNode = Node(x)
        if head is None:
            return newNode
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = newNode

        return head


"""

In the insertAtEnd method, a new node is created with the given data x. If the head is None, indicating an empty list, the new node is returned as the new head. 
Otherwise, we traverse the linked list until we reach the last node. 
Then, we set the next pointer of the last node to the new node, effectively appending it to the end of the list. 
Finally, we return the head of the linked list.

"""


# {
# Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()

        nodes_info = list(map(int, input().split()))
        for i in range(0, len(nodes_info) - 1, 2):
            if nodes_info[i + 1] == 0:
                a.head = Solution().insertAtBegining(a.head, nodes_info[i])
            else:
                a.head = Solution().insertAtEnd(a.head, nodes_info[i])
        printList(a.head)


# } Driver Code Ends
