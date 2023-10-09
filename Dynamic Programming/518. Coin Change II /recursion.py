def count_ways_to_make_change_util(coins, index, target, dp):
    if index == 0:
        return 1 if target & coins[0] == 0 else 0

    if dp[index][target] != -1:
        return dp[index][target]

    not_taken = count_ways_to_make_change_util(coins, index - 1, target, dp)

    taken = 0
    if coins[index] <= target:
        taken = count_ways_to_make_change_util(coins, index, target - coins[index], dp)

    dp[index][target] = not_taken + taken
    return dp[index][target]


def count_ways_to_make_change(coins, target):
    n = len(coins)
    dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
    return count_ways_to_make_change_util(coins, n - 1, target, dp)


def main():
    coins = [1, 2, 3]
    target = 4
    num_ways = count_ways_to_make_change(coins, target)
    print("The total number of ways is", num_ways)


if __name__ == "__main__":
    main()
