class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m.keys():
            return ""
        
        values = self.m[key]
        left, right = 0, len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                result = values[mid][0]  
                left = mid + 1
            else:
                right = mid - 1
        
        return result
        
        

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)