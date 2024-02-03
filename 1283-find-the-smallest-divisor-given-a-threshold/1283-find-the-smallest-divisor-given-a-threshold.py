class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isPossible(mid, nums, threshold):
            total = 0
            for num in nums:
                total += -(-num // mid)

            return total <= threshold

        left, right = 1, max(nums)

        while left <= right:
            mid = left + (right - left) // 2

            if isPossible(mid, nums, threshold):
                right = mid - 1

            else:
                left = mid + 1

        return left
