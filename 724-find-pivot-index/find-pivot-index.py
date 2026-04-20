class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        left = [0] * n
        right = [0] * n

        for i in range(1, n):
            left[i] = left[i - 1] + nums[i - 1]

        for j in range(n - 2, -1, -1):
            right[j] = right[j + 1] + nums[j + 1]
        for k in range(n):
            if left[k] == right[k]:
                return k

        return -1