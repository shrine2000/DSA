class TimeMap:

    def __init__(self):
        self.arr = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.arr[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        element = self.arr.get(key, None)
        if not element or element[0][1]> timestamp:
            return ""
        l, r = 0, len(element) - 1
        while l < r:
            m = (l + r + 1) // 2
            if  element[m][1]<= timestamp:
                l = m 
            else:
                r = m - 1
        return element[l][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
