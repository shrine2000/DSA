class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = 0
        count = 0
        n = len(nums)
        freq = defaultdict(int)
        freq[0] = 1

        for num in nums:
            pre += num
            if pre - k in freq:
                count += freq[pre - k]
            freq[pre] += 1
        return count
