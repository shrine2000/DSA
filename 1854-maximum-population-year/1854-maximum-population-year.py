class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        arr = [0]  * 101
        
        for log in logs:
            arr[log[0] - 1950] += 1
            arr[log[1] - 1950] -= 1
            
        max_pop, curr_sum, max_yr = 0, 0, 0
        
        for yr in range(101):
            curr_sum += arr[yr]
            if curr_sum > max_pop:
                max_pop = curr_sum
                max_yr = 1950 + yr
                
        return max_yr