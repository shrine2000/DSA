from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self._change_recursive(amount, coins, 0)

    def _change_recursive(self, amount: int, coins: List[int], index: int) -> int:
        # Base cases:
        # If the amount is 0, there's one way to make change (no coins used).
        if amount == 0:
            return 1
        # If the amount is negative or we've exhausted all coins, there are no ways to make change.
        if amount < 0 or index >= len(coins):
            return 0

        # Recursive calls:
        # For each coin, we have two choices:
        # 1. Pick the current coin and make a recursive call with reduced amount and same coin.
        # 2. Do not pick the current coin and make a recursive call with the same amount and next coin.
        ways_with_current_coin = self._change_recursive(
            amount - coins[index], coins, index
        )
        ways_without_current_coin = self._change_recursive(amount, coins, index + 1)

        # The total ways is the sum of the ways with and without the current coin.
        return ways_with_current_coin + ways_without_current_coin


# Example usage
def main():
    solution = Solution()
    amount = 5
    coins = [1, 2, 5]
    result = solution.change(amount, coins)
    print("The number of ways to make change is:", result)


if __name__ == "__main__":
    main()
