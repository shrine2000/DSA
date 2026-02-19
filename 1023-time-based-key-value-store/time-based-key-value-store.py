class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        value = self.map.get(key)
        if not value:
            return ""

        left, right = 0, len(value) - 1
        res = ""

        while left <= right:
            mid = left + (right - left) // 2

            if value[mid][0] <= timestamp:
                res = value[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
