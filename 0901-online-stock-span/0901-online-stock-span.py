class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        curr_span = 1
        
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            curr_span += prev_span
        
        self.stack.append((price, curr_span))
        return curr_span