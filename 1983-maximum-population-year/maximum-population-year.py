class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        y = [0] * 101
        for b, d in logs:
            y[b - 1950] += 1
            y[d - 1950] -= 1
        
        max_p = curr_p = 0
        max_y = 0
        
        for i in range(101):
            curr_p += y[i]
            if curr_p > max_p:
                max_p = curr_p
                max_y = i
        
        return max_y + 1950