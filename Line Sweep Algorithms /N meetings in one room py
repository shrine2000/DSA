from typing import List


class Solution:

    def maximumMeetings(self, n, start, end):
        # Pair the start and end times together and sort by end time
        meetings = sorted(zip(start, end), key=lambda x: x[1])

        max_meetings = 0
        last_end_time = 0

        # Iterate over the sorted meetings
        for s, e in meetings:
            if s > last_end_time:
                max_meetings += 1
                last_end_time = e

        return max_meetings


if __name__ == "__main__":
    n = 6
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 6, 7, 9, 9]
    sol = Solution()
    print(sol.maximumMeetings(n, start, end))
