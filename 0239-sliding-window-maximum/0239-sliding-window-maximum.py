class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        q = deque()
        for i in range(n):
            while q and i - q[0] >= k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            
            if i >= k - 1:
                ans.append(nums[q[0]])
                
        return ans
