class MyCalendarTwo:
    def __init__(self):
        self.arr = {}

    def book(self, start: int, end: int) -> bool:
        
        if start not in self.arr:
            self.arr[start] = 0
        if end not in self.arr:
            self.arr[end] = 0
        
        self.arr[start] += 1
        self.arr[end] -= 1
        
        count = 0
        for time in sorted(self.arr.keys()):
            count += self.arr[time]
            if count >= 3:
                self.arr[start] -= 1
                self.arr[end] += 1
                return False
        return True
