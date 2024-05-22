# https://www.lintcode.com/problem/919/
def minMeetingRoomsOptimized(intervals):
    from collections import defaultdict

    events = defaultdict(int)

    # Populate the events dictionary with start and end times
    for interval in intervals:
        events[interval[0]] += 1  # Meeting starts
        events[interval[1]] -= 1  # Meeting ends

    current_rooms = 0
    max_rooms = 0

    # Traverse through the sorted keys (times) of the dictionary
    for time in sorted(events):
        current_rooms += events[time]
        # Update max_rooms if the current count is greater
        max_rooms = max(max_rooms, current_rooms)

    return max_rooms


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(minMeetingRoomsOptimized(intervals))
