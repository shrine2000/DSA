class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min_stack:
            curr_min = self.min_stack[-1]
            self.min_stack.append(min(curr_min, value))
        else:
            self.min_stack.append(value)

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()