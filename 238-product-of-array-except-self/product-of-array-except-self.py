class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        N = len(nums)

        res = [1] * N
        suff = [1] * N
        pref = [1] *N

        for i in range(1, N):
            pref[i] = pref[i - 1] * nums[i - 1]

        for i in range(N - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i+ 1]

        for i in range(N):
            res[i] = suff[i] * pref[i]
        return res 
