class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        # -2, 0, -1
        #  2, 3, -2, 4

        max_prod = res = min_prod = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(num, num * max_prod)
            min_prod = min(num, num * min_prod)
            res = max(max_prod, res)
        return res
