"""

# question - https://leetcode.com/discuss/interview-question/3515163/Google-interview-question

Given array of intervals. find the maximum intersecting interval pair.
For eg. given intervals [1, 100], [1000, 2000], [50, 200], [60, 80] the maximum intersecting interval pair is [60,80].

Solution :

Sorts the intervals based on their start and end points separately.

Checks for overlapping intervals by comparing the start of each interval with the previous interval's end.

The maximum intersecting interval pair is returned. Binary search is used to optimize the process.

"""


def binary_search(arr, target):
    # Binary search in a sorted array
    # Time complexity: O(log n)
    # Space complexity: O(1)
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low


def find_max_intersecting_pair(intervals):
    # Find the maximum intersecting interval pair
    # Time complexity: O(n log n)
    # Space complexity: O(n)
    starts = []
    ends = []

    for interval in intervals:
        start, end = interval
        starts.append(start)
        ends.append(end)

    starts.sort()
    ends.sort()

    total_count = len(intervals)
    non_overlapped_count = 0
    overlapped_count = 0

    for i in range(total_count):
        start, end = intervals[i]

        end_index = binary_search(starts, end)
        start_index = binary_search(ends, start)

        if (
            end_index < len(starts)
            and start_index >= 0
            and starts[end_index] <= end
            and ends[start_index] >= start
        ):
            non_overlapped_count += 1

    overlapped_count = total_count - non_overlapped_count

    if overlapped_count > 0:
        a = intervals[overlapped_count - 1][0]
        b = intervals[overlapped_count - 1][1]
        return [a, b]

    return []


intervals = [[1, 100], [1000, 2000], [50, 200], [60, 80]]
result = find_max_intersecting_pair(intervals)

if result:
    print("Intersecting interval pair:", result)
else:
    print("No intersecting intervals found.")
