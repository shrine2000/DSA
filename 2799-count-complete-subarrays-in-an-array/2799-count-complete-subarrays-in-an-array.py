class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_original = set(nums)
        count = 0

        for i in range(len(nums)):
            distinct_subarray = set()
            for j in range(i, len(nums)):
                distinct_subarray.add(nums[j])
                if len(distinct_subarray) == len(distinct_original):
                    count += 1

        return count
