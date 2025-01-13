# https://algo.monster/liteproblems/759

from typing import List


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"[{self.start}, {self.end}]"


def employee_free_time(schedule: List[List[Interval]]) -> List[Interval]:
    all_intervals = [interval for employee in schedule for interval in employee]
    all_intervals.sort(key=lambda x: x.start)

    # merge overlapping intervals
    merged_intervals = []
    for interval in all_intervals:
        if not merged_intervals or merged_intervals[-1].end < interval.start:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1].end = max(merged_intervals[-1].end, interval.end)

    free_time = []
    for i in range(1, len(merged_intervals)):
        prev_end = merged_intervals[i - 1].end
        curr_start = merged_intervals[i].start
        if prev_end < curr_start:
            free_time.append(Interval(prev_end, curr_start))

    return free_time


if __name__ == "__main__":
    schedule = [
        [Interval(1, 3), Interval(6, 7)],
        [Interval(2, 4)],
        [Interval(2, 5), Interval(9, 12)],
    ]

    free_time = employee_free_time(schedule)
    print(f"Free time intervals: {free_time}")
