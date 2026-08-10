class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 , 2, 3 , 4
        # 1 , 1, 2, 3
        # 24, 12, 4, 1
        n = len(nums)
        left = [1] * n
        right = [1] * n
        res = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for j in range(n - 2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]

        for k in range(0, n):
            res[k] = left[k] * right[k]

        return res
