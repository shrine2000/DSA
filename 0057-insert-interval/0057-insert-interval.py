class Solution:
    def insert(
        self, intervals: List[List[int]], newIntervals: List[int]
    ) -> List[List[int]]:
        merged_intervals = []

        i, n = 0, len(intervals)

        while i < n and intervals[i][1] < newIntervals[0]:
            merged_intervals.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newIntervals[1]:
            newIntervals[0] = min(intervals[i][0], newIntervals[0])
            newIntervals[1] = max(intervals[i][1], newIntervals[1])
            i += 1

        merged_intervals.append(newIntervals)

        while i < n:
            merged_intervals.append(intervals[i])
            i += 1

        return merged_intervals
