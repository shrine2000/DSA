def f(ind, W, wt, val, dp):
    if ind == 0:
        if wt[0] <= W:
            return val[0]
        return 0

    if dp[ind][W] != -1:
        return dp[ind][W]

    not_take = f(ind - 1, W, wt, val, dp)
    take = float("-inf")
    if wt[ind] <= W:
        take = val[ind] + f(ind - 1, W - wt[ind], wt, val, dp)

    dp[ind][W] = max(take, not_take)
    return dp[ind][W]


def knapsack(weight, value, n, max_weight):
    dp = [[-1 for _ in range(max_weight + 1)] for _ in range(n)]

    return f(n - 1, max_weight, weight, value, dp)


if __name__ == "__main__":
    weight = [1, 2, 4, 5]
    value = [5, 4, 8, 6]
    n = len(weight)
    max_weight = 5

    max_value = knapsack(weight, value, n, max_weight)
    print("Maximum value:", max_value)
