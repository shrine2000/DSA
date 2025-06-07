class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        non_over = 0
        prev_end = float("-inf")
        for start, end in intervals:
            if start >= prev_end:
                non_over += 1
                prev_end = end
        return len(intervals) - non_over
