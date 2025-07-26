from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        idx = 0
        n = len(intervals)

        while idx < n and intervals[idx][1] < newInterval[0]:
            res.append(intervals[idx])
            idx += 1

        while idx < n and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1
        res.append(newInterval)

        while idx < n:
            res.append(intervals[idx])
            idx += 1

        return res
