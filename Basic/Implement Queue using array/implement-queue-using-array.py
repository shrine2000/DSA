#User function Template for python3

class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    
    #Function to push an element x in a queue.
    def push(self, x):
        #add code here
        self.stack1.append(x)
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
                
        
        if not self.stack2:
            return -1
            
            
        return self.stack2.pop()
         # add code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   

# } Driver Code Ends