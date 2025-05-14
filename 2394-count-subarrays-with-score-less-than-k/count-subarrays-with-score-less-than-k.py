class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        left = 0
        max_arr = 0
        n = len(nums)
        count = 0
        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum * (right - left + 1) >= k:
                curr_sum -= nums[left]
                left += 1
            count += (right - left) + 1

        return count
