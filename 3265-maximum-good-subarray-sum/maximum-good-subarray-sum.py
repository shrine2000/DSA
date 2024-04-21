class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_left = defaultdict(lambda:inf)
        res = -inf
        cur = 0
        for x in nums:
            prefix_left[x] = min(prefix_left[x], cur)
            cur += x
            
            if x-k in prefix_left:
                res = max(res, cur - prefix_left[x-k])
            if x+k in prefix_left:
                res = max(res, cur - prefix_left[x+k])
        return res if res != -inf else 0
                
        
        