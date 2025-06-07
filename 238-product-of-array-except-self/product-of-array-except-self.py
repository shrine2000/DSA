class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        suf = [1] * n

        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]

        print(pre)

        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        print(suf)

        answer = [0] * n
        for i in range(n):
            answer[i] = pre[i] * suf[i]
        return answer
