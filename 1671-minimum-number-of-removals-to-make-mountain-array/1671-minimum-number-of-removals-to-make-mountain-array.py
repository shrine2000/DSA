class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        l, r = [1] * n, [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    l[i] = max(l[i], 1 + l[j])

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    r[i] = max(r[i], 1 + r[j])

        m = 0

        for i in range(n):
            if l[i] > 1 and r[i] > 1:
                m = max(m, l[i] + r[i] - 1)

        return n - m if m > 0 else -1
