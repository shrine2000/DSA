class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        curr_sum = 0
        for num in nums:
            curr_sum += num
            needed = curr_sum -k
            if needed in prefix_sum:
                answer += prefix_sum.get(needed)
            prefix_sum[curr_sum] += 1
        return answer
