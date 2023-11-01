#User function Template for python3
class Solution:
    def maxSumIS(self, Arr, n):
        ms = [0] * n
        
        
        for i in range(n):
            ms[i] = Arr[i]
            for j in range(i):
                if Arr[i] > Arr[j]:
                    ms[i] = max(ms[i], ms[j] + Arr[i])
            
        res = max(ms)
            
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends