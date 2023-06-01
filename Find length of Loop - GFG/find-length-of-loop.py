#User function Template for python3

'''
Structure of node

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''

#Function to find the length of a loop in the linked list.
def countNodesinLoop(head):
    # Initialize two pointers, slow and fast
    slow = head
    fast = head

    # Move slow pointer by one and fast pointer by two
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If slow and fast pointers meet, there is a loop
        if slow == fast:
            # Count the number of nodes in the loop
            count = 1
            temp = slow.next
            while temp != slow:
                count += 1
                temp = temp.next
            return count

    # If loop is not found, return 0
    return 0
    
    """ 
    
    We initialize a variable count to 1 because we have already identified one node in the loop (the current slow node).
    We create a temporary node temp and assign it the value of slow.next. This allows us to traverse the loop and count the number of nodes in it.
    The while loop iterates as long as temp is not equal to slow, indicating that we have completed a full loop traversal.
    Inside the loop, we increment the count variable by 1 to account for each node we encounter in the loop.
    We update temp to its next node (temp = temp.next) to continue traversing the loop.
    Once the loop ends, we have counted all the nodes in the loop, so we return the final value of count.
    
    """



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
    
    #connects last node to node at position pos from begining.
    def loopHere(self,pos):
        if pos==0:
            return
        
        walk = self.head
        for i in range(1,pos):
            walk = walk.next
        
        self.tail.next = walk

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))
        
        LL.loopHere(int(input()))
        
        print(countNodesinLoop(LL.head))

# } Driver Code Ends