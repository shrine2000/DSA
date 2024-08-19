class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_sum_count = {}
        prefix_sum_count[0] = 1
        
        for num in nums:
            prefix_sum += num
            target = prefix_sum - goal
            if target in prefix_sum_count:
                count += prefix_sum_count[target]
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1
            else:
                prefix_sum_count[prefix_sum] = 1
        return count
    