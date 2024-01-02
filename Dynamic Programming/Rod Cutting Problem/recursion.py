def unbounded_knapsack(price, length, maxLength, N):
    # Create a memoization table to store computed values
    memo = [[-1 for _ in range(maxLength + 1)] for _ in range(N + 1)]

    # Base Case: If the rod length is zero or the maximum length is zero, the profit is zero.
    if N == 0 or maxLength == 0:
        return 0

    # Check if the result for the current state is already computed
    if memo[N][maxLength] != -1:
        return memo[N][maxLength]

    # Check if the current rod length can be included in the cut
    if length[N - 1] <= maxLength:
        # Calculate the maximum profit by either including or excluding the current rod length
        memo[N][maxLength] = max(
            price[N - 1]
            + unbounded_knapsack(price, length, maxLength - length[N - 1], N),
            unbounded_knapsack(price, length, maxLength, N - 1),
        )
    else:
        # If the current rod length is too long to be included, skip it
        memo[N][maxLength] = unbounded_knapsack(price, length, maxLength, N - 1)

    return memo[N][maxLength]


price = [2, 4, 6]
length = [5, 11, 13]
maxLength = 10
N = len(price)
result = unbounded_knapsack(price, length, maxLength, N)
print("Maximum profit:", result)
