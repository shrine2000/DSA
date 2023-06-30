#User function Template for python3

class Solution:
    def NthRoot(self, n, m):
        if n == 1:
            return m

        left, right = 0, m
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            x = mid

            for i in range(1, n):
                x *= mid
                if x > m:
                    break

            if x == m:
                ans = mid
                break
            elif x > m:
                right = mid - 1
            else:
                left = mid + 1

        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends