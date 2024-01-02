# User function Template for python3
class Solution:
    def print2largest(self, arr, n):
        max1 = -1
        max2 = -1

        # Traverse the array and update max1 and max2
        for i in range(n):
            # If current element is greater than max1,
            # update max2 and max1
            if arr[i] > max1:
                max2 = max1
                max1 = arr[i]
            # If current element is between max1 and max2,
            # update max2
            elif arr[i] > max2 and arr[i] != max1:
                max2 = arr[i]

        return max2


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
