from typing import List


class Solution:
    @staticmethod
    def maximumTripletValue(nums: List[int]) -> int:
        n = len(nums)
        prfx = [0] * n
        sufx = [0] * n

        prfx[0] = nums[0]
        for i in range(1, n):
            prfx[i] = max(prfx[i - 1], nums[i])

        sufx[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            sufx[i] = max(sufx[i + 1], nums[i])

        res = 0

        for j in range(1, n - 1):
            res = max(res, (prfx[j - 1] - nums[j]) * sufx[j + 1])

        return res


if __name__ == "__main__":
    solution = Solution()
    nums1 = [12, 6, 1, 2, 7]
    nums2 = [1, 10, 3, 4, 19]
    nums3 = [1, 2, 3]

    print(solution.maximumTripletValue(nums1))
    print(solution.maximumTripletValue(nums2))
    print(solution.maximumTripletValue(nums3))
