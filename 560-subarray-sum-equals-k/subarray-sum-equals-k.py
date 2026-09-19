class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        running_sum = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        for num in nums:
            running_sum += num
            needed_prefix = running_sum - k
            answer += prefix[needed_prefix]
            prefix[running_sum] += 1
        return answer