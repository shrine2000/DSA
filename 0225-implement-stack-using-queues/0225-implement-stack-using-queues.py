class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop()
        return -1

    def top(self) -> int:
        if not self.empty():
            return self.stack[-1]
        return -1

    def empty(self) -> bool:
        return len(self.stack) == 0
