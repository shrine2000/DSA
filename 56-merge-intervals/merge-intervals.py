class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])


        N = len(intervals)
        merged = []
        prev = intervals[0]

        for i in range(1, N):
            # Sort by start; compare curr.start <= prev.end; merge by prev.end = max(prev.end, curr.end)
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                merged.append(prev)
                prev = intervals[i]
        merged.append(prev)
        return merged


