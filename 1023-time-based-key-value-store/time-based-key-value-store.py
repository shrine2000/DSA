class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""

        ts_list = self.timestamps[key]
        val_list = self.values[key]

        left, right = 0, len(ts_list) - 1
        best_idx = -1
        while left <= right:
            mid = (left + right) // 2
            if ts_list[mid] <= timestamp:
                best_idx = mid
                left = mid + 1
            else:
                right = mid - 1
        return val_list[best_idx] if best_idx != -1 else ""
                