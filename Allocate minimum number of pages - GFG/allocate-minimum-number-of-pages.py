class Solution:
    # Function to find minimum number of pages.
    def findPages(self, A, N, M):
        def isPossible(pages, N, M, max_pages):
            students = 1
            curr_pages = 0

            for i in range(N):
                if curr_pages + A[i] > max_pages:
                    students += 1
                    curr_pages = A[i]
                else:
                    curr_pages += A[i]

                if students > M:
                    return False

            return True

        if N < M:
            return -1

        start = max(A)
        end = sum(A)
        result = float("inf")

        while start <= end:
            mid = start + (end - start) // 2

            if isPossible(A, N, M, mid):
                result = min(result, mid)
                end = mid - 1
            else:
                start = mid + 1

        return result


# {
# Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        m = int(input())

        ob = Solution()

        print(ob.findPages(arr, n, m))
# } Driver Code Ends
