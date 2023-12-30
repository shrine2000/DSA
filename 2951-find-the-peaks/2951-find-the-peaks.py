from typing import List

class Solution:
    def findPeaks(self, m: List[int]) -> List[int]:
        peak_indices = []
        
        n = len(m)
        
        for i in range(1, n - 1):
            if m[i] > m[i-1] and m[i] > m[i+1]: 
                peak_indices.append(i) 
        
        return peak_indices
