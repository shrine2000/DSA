class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        l = heapq.nlargest(3, nums)
        s = heapq.nsmallest(3, nums)
        
        p = [(s, l) for s, l in zip(s, reversed(l))]
        
        m = min(l - s for s, l in p)
        
        return m