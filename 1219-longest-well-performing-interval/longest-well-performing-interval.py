from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        max_length = 0
        prefix_sum = 0
        prefix_map = {}
        
        for i in range(n):
            if hours[i] > 8:
                prefix_sum += 1
            else:
                prefix_sum -= 1
                
            if prefix_sum > 0:
                max_length = i + 1
            else:
                if prefix_sum - 1 in prefix_map:
                    max_length = max(max_length, i - prefix_map[prefix_sum - 1])
                    
                if prefix_sum not in prefix_map:
                    prefix_map[prefix_sum] = i
        return max_length