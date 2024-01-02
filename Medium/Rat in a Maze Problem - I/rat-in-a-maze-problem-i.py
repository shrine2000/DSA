# User function Template for python3


class Solution:
    def findPath(self, m, n):
        def backtrack(i, j, path):
            if i == n - 1 and j == n - 1:
                paths.append(path)
                return

            for x, y, move in [
                (i + 1, j, "D"),
                (i - 1, j, "U"),
                (i, j + 1, "R"),
                (i, j - 1, "L"),
            ]:
                if 0 <= x < n and 0 <= y < n and m[x][y] == 1 and (x, y) not in visited:
                    visited.add((x, y))
                    backtrack(x, y, path + move)
                    visited.remove((x, y))

        paths = []
        visited = set()
        if m[0][0] == 1:
            visited.add((0, 0))
            backtrack(0, 0, "")

        return sorted(paths)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        matrix = [[0 for i in range(n[0])] for j in range(n[0])]
        k = 0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k += 1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            for x in result:
                print(x, end=" ")
            print()
# } Driver Code Ends
