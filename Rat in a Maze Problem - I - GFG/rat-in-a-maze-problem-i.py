#User function Template for python3

class Solution:
    def findPath(self, m, n):
        def backtrack(i, j, a, n, ans, move, vis):
            if i == n - 1 and j == n - 1:
                ans.append(move)

            # Downward
            if i + 1 < n and not vis[i + 1][j] and a[i + 1][j] == 1:
                vis[i][j] = 1
                backtrack(i + 1, j, a, n, ans, move + 'D', vis)
                vis[i][j] = 0

            # Left
            if j - 1 >= 0 and not vis[i][j - 1] and a[i][j - 1] == 1:
                vis[i][j] = 1
                backtrack(i, j - 1, a, n, ans, move + 'L', vis)
                vis[i][j] = 0

            # Right
            if j + 1 < n and not vis[i][j + 1] and a[i][j + 1] == 1:
                vis[i][j] = 1
                backtrack(i, j + 1, a, n, ans, move + 'R', vis)
                vis[i][j] = 0

            # Upwards
            if i - 1 >= 0 and not vis[i - 1][j] and a[i - 1][j] == 1:
                vis[i][j] = 1
                backtrack(i - 1, j, a, n, ans, move + 'U', vis)
                vis[i][j] = 0

        ans = []
        vis = [[False for j in range(len(m[0]))] for i in range(len(m))]
        if m[0][0] == 1:
            backtrack(0, 0, m, n, ans, "", vis)

        return sorted(ans)  

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends