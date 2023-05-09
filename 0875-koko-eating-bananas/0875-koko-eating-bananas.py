class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_speed = 1
        max_speed = max(piles)
        
        while min_speed < max_speed: 
            mid_speed = (min_speed + max_speed) // 2
            total_hours = sum(math.ceil(pile / mid_speed) for pile in piles)
            if total_hours > h:
                min_speed = mid_speed + 1
            else: 
                max_speed = mid_speed
                
        return min_speed
        