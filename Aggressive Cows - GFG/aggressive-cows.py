# User function Template for python3


class Solution:
    def isPossible(self, stalls, cows, distance):
        count = 1
        last_position = stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i] - last_position >= distance:
                count += 1
                last_position = stalls[i]

                if count == cows:
                    return True

        return False

    def solve(self, n, k, stalls):
        stalls.sort()

        low = 1

        high = stalls[-1] - stalls[0]

        result = 0

        while low <= high:
            mid = (low + high) // 2

            if self.isPossible(stalls, k, mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result


# {
# Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while T > 0:
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
