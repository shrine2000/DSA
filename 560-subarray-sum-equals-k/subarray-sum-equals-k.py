class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}

        res = 0
        s = 0
        for num in nums:
            s += num
            res += count.get(s - k, 0)
            count[s] = count.get(s, 0) + 1
        return res
