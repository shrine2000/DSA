class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        max_product = float("-inf")
        result = [-1, -1]

        for j, x in enumerate(nums):
            y = target - x

            if y in seen and y != x:
                i = seen[y]
                product = x * y

                if product > max_product:
                    max_product = product
                    result = [i, j] if nums[i] > x else [j, i]

            seen[x] = j

        return result