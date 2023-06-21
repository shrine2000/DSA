class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = left + (right  - left) // 2
            required_days = self.calculateRequiredDays(weights, mid)
            
            if required_days <= days:
                right = mid
            else:
                left = mid + 1
            
        return left
        
        
    def calculateRequiredDays(self, weights: List[int], capacity: int) -> int:
        cur_day = 1
        remaining_cap = capacity
        
        for weight in weights:
            if weight > remaining_cap :
                cur_day += 1
                remaining_cap = capacity
                
            remaining_cap -= weight
            
        
        return cur_day
        
        