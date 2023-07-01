#User function Template for python3


class Solution:
    def InfixtoPostfix(self, exp):
        precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

        stack = []
        postfix = ""

        for char in exp:
            if char.isalnum():  # Operand
                postfix += char
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()  # Discard the opening parenthesis
            else:  # Operator
                while stack and stack[-1] != '(' and precedence[char] <= precedence.get(stack[-1], 0):
                    postfix += stack.pop()
                stack.append(char)

        while stack and stack[-1] != '(':
            postfix += stack.pop()

        return postfix


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends