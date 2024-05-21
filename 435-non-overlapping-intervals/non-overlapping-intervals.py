class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[1])
        prev, count = intervals[0][1], 1 
        for interval in intervals[1:]:
            if interval[0] >= prev:
                prev = interval[1]
                count += 1
        return len(intervals) - count