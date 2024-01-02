# User function Template for python3


class Solution:
    def bubbleSort(self, arr, n):
        # Traverse through all array elements
        for i in range(len(arr) - 1):
            # Last i elements are already in place
            for j in range(0, len(arr) - i - 1):
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i, end=" ")
        print()

# } Driver Code Ends
