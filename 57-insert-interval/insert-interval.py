class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        N = len(intervals)
        i = 0
        res = []

        # 1. intervals[i].end < new.start
        # → completely BEFORE → append

        while i < N and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2. intervals[i].start <= end
        # → OVERLAP → merge

        temp = [0, 0]
        while i < N and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+=1
        res.append(newInterval)

        # 3. everything remaining
        # → completely AFTER → append

        while i < N:
            res.append(intervals[i])
            i += 1
        return res
