class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 , 2, 3 , 4
        # 1 , 1, 2, 3
        # 24, 12, 4, 1
        n = len(nums)
        res = [1] * n

        prefix = [1] * n
        suffix = [1] * n
        res = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res 
