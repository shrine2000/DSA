class Solution:
    def maxSlidingWindow(self, nm: List[int], k: int) -> List[int]:
        a = []
        n = len(nm)
        q = deque()
        for i in range(n):
            while q and i - q[0] >= k:
                q.popleft()
            while q and nm[q[-1]] < nm[i]:
                q.pop()
            q.append(i)
            
            if i >= k - 1:
                a.append(nm[q[0]])
                
        return a
