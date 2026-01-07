class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [[1,2],[2,3],[1,3],[3,4]]
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                removals += 1
            else:
                prev_end = end
        return removals
