# User function Template for python3


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, arr, n):
        # Calculating the value-to-weight ratio for each item.
        for item in arr:
            item.value_per_weight = item.value / item.weight

        # Sorting items based on value-to-weight ratio in descending order.
        arr.sort(key=lambda x: x.value_per_weight, reverse=True)

        total_value = 0
        current_weight = 0

        for item in arr:
            if current_weight + item.weight <= W:
                # If the entire item can be added to the knapsack.
                total_value += item.value
                current_weight += item.weight
            else:
                # If only a fraction of the item can be added to the knapsack.
                remaining_capacity = W - current_weight
                fraction = remaining_capacity / item.weight
                total_value += fraction * item.value
                break  # Knapsack is full, exit loop.

        return total_value


# {
# Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == "__main__":
    test_cases = int(input())
    for cases in range(test_cases):
        n, W = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        arr = [Item(0, 0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2 * i]
            arr[i].weight = info[2 * i + 1]

        ob = Solution()
        print("%.2f" % ob.fractionalknapsack(W, arr, n))

# } Driver Code Ends
