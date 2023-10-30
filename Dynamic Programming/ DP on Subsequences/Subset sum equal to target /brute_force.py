from typing import List


class Solution:
    def isSubsetSum(self, N: int, arr: List[int], target_sum: int) -> bool:
        def helper(arr: List[int], k: int, n: int) -> bool:
            if n < 0 or k < 0:
                return False

            if k == 0:
                return True

            pick: bool = helper(arr, k - arr[n], n - 1)
            not_pick: bool = helper(arr, k, n - 1)

            return pick or not_pick

        return helper(arr, target_sum, N - 1)


if __name__ == "__main__":
    arr: List[int] = [3, 34, 4, 12, 5, 2]
    target_sum: int = 9
    print(Solution().isSubsetSum(len(arr), arr, target_sum))
