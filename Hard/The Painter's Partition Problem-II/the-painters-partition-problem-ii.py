# User function Template for python3


class Solution:
    def minTime(self, arr, n, k):
        left = max(arr)
        right = sum(arr)

        while left < right:
            mid = left + (right - left) // 2

            requiredPainters = self.countPainters(arr, mid)
            if requiredPainters <= k:
                right = mid
            else:
                left = mid + 1

        return left

    def countPainters(self, arr, target):
        painters = 1
        curr_sum = 0

        for i in arr:
            curr_sum += i

            if curr_sum > target:
                curr_sum = i
                painters += 1

        return painters


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        str = input().split()
        k = int(str[0])
        n = int(str[1])
        arr = input().split()
        for itr in range(n):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.minTime(arr, n, k))
# } Driver Code Ends
