class MinStack:

    def __init__(self):
        self.list1 = []
        

    def push(self, val: int) -> None:
        self.list1.append(val)

    def pop(self) -> None:
        del self.list1[-1]

    def top(self) -> int:
        return self.list1[-1]

    def getMin(self) -> int:
        return min(self.list1)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()