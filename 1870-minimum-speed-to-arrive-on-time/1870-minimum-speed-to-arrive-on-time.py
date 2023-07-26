class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
         
        def calculate_time(speed):
            total_time = 0
            for i in range(len(dist) - 1):
                total_time += (dist[i] + speed - 1) // speed
            total_time += dist[-1] / speed
            return total_time
        
        left, right = 1, 10**7  
        
        while left <= right:
            mid = (left + right) // 2
            total_time = calculate_time(mid)
            
            if total_time <= hour:
                right = mid - 1
            else:
                left = mid + 1
        
        if left <= 10**7:   
            return left
        else:
            return -1

 