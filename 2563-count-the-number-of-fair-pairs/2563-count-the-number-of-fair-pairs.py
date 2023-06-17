class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        count = 0
        i = 0
        low = high = len(nums) - 1

        while i < high:
            low = max(i, low)
            while low > i and nums[i] + nums[low] >= lower:
                low -= 1

            while high > low and nums[i] + nums[high] > upper:
                high -= 1

            count += high - low

            i += 1

        return count
