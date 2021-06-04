import sys


class NotEnoughOperandsException(Exception):

    pass


class UnknownOperatorException(Exception):

    pass


class TokenParseException(Exception):

    pass


class MatchingBracketNotFound(Exception):

    pass


class SimpleCalculator:

    EXPONENT = "^"
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "*"
    DIVISION = "/"
    MODULO = "%"
    OPENING_ROUND_BRACKET = "("
    CLOSING_ROUND_BRACKET = ")"

    OPERATORS = f"{EXPONENT}{ADDITION}{SUBTRACTION}{MULTIPLICATION}{DIVISION}{MODULO}"

    def __init__(self, expression):

        self.expression = expression.replace(" ", "")

    def determine_precedence(self, operator_string):

        if operator_string == self.EXPONENT:
            return 3
        elif (
            operator_string == self.DIVISION or operator_string == self.MULTIPLICATION or operator_string == self.MODULO
        ):
            return 2
        elif operator_string == self.ADDITION or operator_string == self.SUBTRACTION:
            return 1
        return 0

    def normalize_infix_pattern(self, pattern):

        normalized_string = ""
        for char in pattern:
            if char in self.OPERATORS:
                normalized_string += f" {char} "
            elif char == self.OPENING_ROUND_BRACKET:
                normalized_string += f"{self.OPENING_ROUND_BRACKET} "
            elif char == self.CLOSING_ROUND_BRACKET:
                normalized_string += f" {self.CLOSING_ROUND_BRACKET}"
            else:
                normalized_string += char
        return normalized_string

    def convert_to_postfix(self, expression):

        stack = []
        postfix_string = ""
        expression = self.normalize_infix_pattern(expression)
        for token in expression.split(" "):
            if token not in self.OPERATORS and token.isdigit():
                postfix_string += token + " "
            elif token == self.OPENING_ROUND_BRACKET:
                stack.append(token)
            elif token == self.CLOSING_ROUND_BRACKET:
                while stack and stack[-1] != self.OPENING_ROUND_BRACKET:
                    postfix_string += stack.pop() + " "
                try:
                    stack.pop()
                except IndexError:
                    raise MatchingBracketNotFound("Invalid Expression, matching opening bracket not found")
            elif token in self.OPERATORS:
                if not stack:
                    stack.append(token)
                else:
                    if self.determine_precedence(token) > self.determine_precedence(stack[-1]):
                        stack.append(token)
                    elif (
                        self.determine_precedence(token) == self.determine_precedence(stack[-1])
                        and token == self.EXPONENT
                    ):
                        stack.append(token)
                    else:
                        while stack and self.determine_precedence(token) <= self.determine_precedence(stack[-1]):
                            postfix_string += stack.pop() + " "
                        stack.append(token)
            elif token == " ":
                pass
            else:
                raise TokenParseException("Token cannot be parsed %s", token)
        while stack:
            postfix_string += stack.pop() + " "
        if self.OPENING_ROUND_BRACKET in postfix_string:
            raise MatchingBracketNotFound('Invalid Expression, matching closing not found')
        return postfix_string.rstrip()

    def make_result(self, b, operator, a):

        b, a = float(b), float(a)

        if operator == self.ADDITION:
            result = b + a
        elif operator == self.DIVISION:
            result = b / a
        elif operator == self.MULTIPLICATION:
            result = b * a
        elif operator == self.EXPONENT:
            result = b ** a
        elif operator == self.SUBTRACTION:
            result = b - a
        elif operator == self.MODULO:
            result = b % a
        else:
            raise UnknownOperatorException("Operator is unknown %s", operator)
        return result

    def evaluate_postfix_expression(self):

        postfix_expression = self.convert_to_postfix(self.expression).split(" ")
        stack = []
        for token in postfix_expression:
            if token in self.OPERATORS:
                a = stack.pop()
                try:
                    b = stack.pop()
                except IndexError:
                    raise NotEnoughOperandsException(
                        "There are operators left, which means there aren't enough operands in the expression"
                    )
                result = self.make_result(b, token, a)
                stack.append(result)
            else:
                stack.append(token)
        return stack[-1]


if __name__ == "__main__":
    try:
        input_expression = sys.argv[1]
    except IndexError:
        raise SystemExit("No expression passed, exiting.")
    simple_calculator = SimpleCalculator(input_expression)
    sys.stdout.write(f"POSTFIX EXPRESSION: {simple_calculator.convert_to_postfix(simple_calculator.expression)}\n")
    sys.stdout.write(f"RESULT: {simple_calculator.evaluate_postfix_expression()}\n")
