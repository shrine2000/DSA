import queue

class Solution:
    def minimumSum(self, num: int) -> int:
        pq = queue.PriorityQueue()
        digits = [int(digit) for digit in str(num)]
        for digit in digits:
            pq.put(digit)

            
        # 2932 => 2239 => [29, 23]
        # 4009 => 0049 => [9, 4]
        
        smallest1 = pq.get()
        smallest2 = pq.get()
        largest1 = pq.get()
        largest2 = pq.get()
        
        new1 = smallest1 * 10 + largest1  
        new2 = smallest2 * 10 + largest2   
        
        return new1 + new2
