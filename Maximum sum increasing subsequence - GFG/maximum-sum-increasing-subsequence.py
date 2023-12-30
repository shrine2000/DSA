class Solution:
    def maxSumIS(self, Arr, n):
        ms = [0] * n
        idx = [-1] * n
        
        
        for i in range(n):
            ms[i] = Arr[i]
            for j in range(i):
                if Arr[i] > Arr[j]:
                    ms[i] = max(ms[i], ms[j] + Arr[i])
                    idx[i] = i
            
        res = max(ms)
            
        return res




if __name__ == '__main__':
    Arr = [1, 101, 2, 3, 100]
    N = 5
    sol = Solution()
    ms = sol.maxSumIS(Arr, N)
    print(ms)


