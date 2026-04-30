class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i, v in enumerate(arr):
            missing = v - (i + 1)
            if missing >= k:
                return i + k
            
        return len(arr) + k
