from typing import List


def infix_to_prefix(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    output = []
    operators = []

    def apply_operator():
        output.append(operators.pop())

    for token in expression:
        if token.isalnum():
            output.append(token)


if __name__ == "__main__":
    pass
