class Solution:
     def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        priority_queue = []
        for num in nums:
            heapq.heappush(priority_queue, num)
        
        max_len = 1
        current_len = 1
        prev_num = heapq.heappop(priority_queue)
        
        while priority_queue:
            num = heapq.heappop(priority_queue)
            if num == prev_num + 1:
                current_len += 1
            elif num != prev_num:
                max_len = max(max_len, current_len)
                current_len = 1
            prev_num = num
        
        return max(max_len, current_len)