class MyQueue:

    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def push(self, x: int) -> None:
        self.stack_push.append(x)
        
    def pop(self) -> int:
        self.peek()
        return self.stack_pop.pop()

    def peek(self) -> int:
        if len(self.stack_pop) == 0:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop[-1]

    def empty(self) -> bool:
        return len(self.stack_pop) + len(self.stack_push) == 0
