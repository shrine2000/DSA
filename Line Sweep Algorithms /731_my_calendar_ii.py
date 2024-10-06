from collections import defaultdict


class MyCalendarTwo:

    def __init__(self):
        self.arr = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.arr[start] += 1
        self.arr[end] -= 1

        overlap = 0
        for time in sorted(self.arr.keys()):
            overlap += self.arr[time]
            if overlap >= 3:
                self.arr[start] -= 1
                self.arr[end] += 1
                if self.arr[start] == 0:
                    del self.arr[start]
                if self.arr[end] == 0:
                    del self.arr[end]
                return False

        return True


if __name__ == "__main__":
    obj = MyCalendarTwo()
    print(obj.book(10, 20))  # True,
    print(obj.book(15, 25))  # True,
    print(obj.book(20, 30))  # True,
    print(obj.book(5, 15))  # True,
    print(obj.book(10, 30))  # False,
