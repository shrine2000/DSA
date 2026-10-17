class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (
                    intervals[i][0] <= intervals[j][1]
                    and intervals[j][0] <= intervals[i][1]
                ):
                    count += 1
        return count
