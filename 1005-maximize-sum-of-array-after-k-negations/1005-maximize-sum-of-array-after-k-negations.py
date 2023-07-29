import queue

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        pq = queue.PriorityQueue()
        
        for num in nums:
            pq.put(num)

        while k > 0:
            smallest = pq.get()
            pq.put(-smallest)
            k -= 1

        ans = 0

        while not pq.empty():
            ans += pq.get()   
        return ans
