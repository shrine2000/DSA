def infix_to_postfix(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    output = []
    operators = []

    def apply_operator():
        output.append(operators.pop())

    for token in expression:
        if token.isalnum():  # Operand
            output.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                apply_operator()
            operators.pop()  # Pop the '('
        elif token in precedence:  # Operator
            while (
                operators
                and operators[-1] != "("
                and precedence[operators[-1]] >= precedence[token]
            ):
                apply_operator()
            operators.append(token)

    while operators:
        apply_operator()

    return " ".join(output)


if __name__ == "__main__":
    infix_expression = "(2 + 3) * 4"
    postfix_expression = infix_to_postfix(infix_expression.split())
    print(f"Infix: {infix_expression}")
    print(f"Postfix: {postfix_expression}")

    infix_expression_complex = "a + b * (c ^ d - e) / f"
    postfix_expression_complex = infix_to_postfix(infix_expression_complex.split())
    print(f"Infix: {infix_expression_complex}")
    print(f"Postfix: {postfix_expression_complex}")
