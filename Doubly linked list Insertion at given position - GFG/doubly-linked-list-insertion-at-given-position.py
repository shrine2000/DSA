# Your task is to complete this function
# function should add a new node after the pth position
# function shouldn't print or return any data

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''
#Function to insert a new node at given position in doubly linked list.
def addNode(head, p, data):
    
    temp = head
    while p!=0:
        temp = temp.next
        p -= 1
        
    n = Node(data)
    
    if temp.next is None:
        n.prev = temp
        temp.next = n
    
    else:
        n.next = temp.next
        temp.next = n
        temp.next.prev = n
        n.prev = temp
    
#{ 
 # Driver Code Starts
class Node:
	def __init__(self, data):
		self.data = data
		
		
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, new_data):
		new_node = Node(new_data)
		if(self.head == None):
		    self.head = new_node
		    self.tail = new_node
		    return
		
		self.tail.next = new_node
		new_node.prev = self.tail
		self.tail = new_node
		return
		
	def printList(self, node):
		while(node.next is not None):
			node = node.next
		while node.prev is not None:
		    node = node.prev
		while(node is not None):
		    print(node.data, end=" ")
		    node = node.next
		print()
		
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = map(int, input().strip().split())
        llist = DoublyLinkedList()
        for e in arr:
            llist.add(e)
            
        pos,data = map(int, input().strip().split())
        
        addNode(llist.head, pos, data)
        llist.printList(llist.head)

# } Driver Code Ends