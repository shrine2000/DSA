from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = set()
        for s, e in nums:
            for p in range(s, e + 1):
                points.add(p)
        return len(points)
