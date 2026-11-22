class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        count = 0

        def avg(arr):
            return (arr[0] + arr[1]) / 2

        N = len(nums)
        if N == 0:
            return 0

        if N == 1:
            return 1

        for i in range(N):
            if i == 0:
                ngbr = nums[i + 1]
                if nums[i] >= ngbr:
                    count += 1

            elif i == N - 1:
                ngbr = nums[i - 1]
                if nums[i] >= ngbr:
                    count += 1
            else:
                if nums[i] >= avg([nums[i - 1], nums[i + 1]]):
                    count += 1
        return count
