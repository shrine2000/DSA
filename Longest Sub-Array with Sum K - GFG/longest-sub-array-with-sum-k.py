class Solution:
    # TODO

    def lenOfLongSubarr(self, a, n, k):
        n = len(a)

        preSumMap = {}
        Sum = 0
        maxLen = 0
        for i in range(n):
            Sum += a[i]

            if Sum == k:
                maxLen = max(maxLen, i + 1)

            rem = Sum - k

            if rem in preSumMap:
                length = i - preSumMap[rem]
                maxLen = max(maxLen, length)

            if Sum not in preSumMap:
                preSumMap[Sum] = i

        return maxLen


# {
# Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))


# } Driver Code Ends
