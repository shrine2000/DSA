class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in { "+", "-", "*", "/"}:
                b, a = stack.pop(), stack.pop()
                if token == "+":
                    res = a + b
                elif token == "-":
                    res = a - b
                elif token == "*":
                    res = a * b
                else:
                    res = int( a / b)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]
