#User function Template for python3
class Solution:
    def maxSumIS(self, Arr, n):
        # Initialize a list to store the maximum sum ending at each index
        max_sum = [0] * n

        for i in range(n):
            max_sum[i] = Arr[i]  # Initialize with the element itself

            for j in range(i):
                if Arr[i] > Arr[j]:
                    max_sum[i] = max(max_sum[i], Arr[i] + max_sum[j])

        # Find the maximum value in the max_sum list
        result = max(max_sum)

        return result


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