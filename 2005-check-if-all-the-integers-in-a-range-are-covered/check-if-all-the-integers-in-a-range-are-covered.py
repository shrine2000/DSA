class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        res = False
        for value in range(left, right + 1):
            if not any(start <= value <= end for start, end in ranges):
                return False
        return True
