from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    
    
    # 3 approaches mentioned here - https://www.codingninjas.com/codestudio/problem-details/find-pair-with-a-given-sum-in-a-doubly-linked-list_1164172
    
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        hash_set = set()
        pairs = []

        ptr1 = head
        while ptr1 is not None:
            val = ptr1.data
            complement = target - val

            if complement in hash_set:
                pairs.append([complement, val])
            else:
                hash_set.add(val)

            ptr1 = ptr1.next
            
        pairs.sort()

        return pairs

        


#{ 
 # Driver Code Starts
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class doublyLL:
    def __init__(self):
        self.head=None

    def insert(self,tail,data):
        head=self.head

        node=Node(data)

        if not head:

            self.head=node
            return node

        tail.next=node
        node.prev=tail
        return node

def displayList(head):
    while head:
        print(head.data,end=' ')
        pvs=head
        head=head.next
    print()

    while pvs:
        print(pvs.data,end=' ')
        pvs=pvs.prev


if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        target = int(input())
        n=int(input())
        arr=[int(x) for x in input().split()]

        dll=doublyLL()

        tail=None

        for nodeData in arr:
            tail=dll.insert(tail,nodeData)

        obj = Solution()
        ans = obj.findPairsWithGivenSum(target, dll.head)
        if (len(ans)== 0):
            print(-1)
        else:
        
            for i in range(len(ans)):
                print( "(" + str(ans[i][0]) + "," + str(ans[i][1])+ ")" , end = ' ')
                
            print()
                     
            
        


# } Driver Code Ends