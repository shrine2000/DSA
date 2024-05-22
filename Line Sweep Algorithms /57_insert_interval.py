from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # Initialize the list to hold merged intervals
        merged_intervals = []

        # Add the new interval to the list of existing intervals
        intervals.append(newInterval)

        # Sort the intervals based on their start time
        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            # If the list of merged intervals is empty or there is no overlap, append the interval
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                # If there is an overlap, merge the intervals
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        return merged_intervals


# Time Complexity: O((N+1) log (N+1)) due to the sorting step
# Space Complexity: O(N) for storing the merged intervals

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    result = sol.insert(intervals, newInterval)
    assert result == [[1, 2], [3, 10], [12, 16]]
