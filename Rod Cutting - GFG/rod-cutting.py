# User function Template for python3


class Solution:
    def cutRod(self, price, n):
        # Initialize a list to store maximum revenue for each length
        max_revenue = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(i):
                max_revenue[i] = max(max_revenue[i], price[j] + max_revenue[i - j - 1])

        return max_revenue[n]


# {
# Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())

    while T > 0:
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
