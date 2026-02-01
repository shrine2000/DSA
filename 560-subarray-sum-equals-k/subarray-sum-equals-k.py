class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_freq = {0: 1}
        running_sum = 0
        count = 0

        for num in nums:
            running_sum += num

            if running_sum - k in prefix_freq:
                count += prefix_freq[running_sum - k]

            prefix_freq[running_sum] = prefix_freq.get(running_sum, 0) + 1

        return count
