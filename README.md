# simple-calculator
A Simple Command Line Calculator

# About
This is a simple command line calculator that converts the infix expression to postfix expression and then evaluates the postfix expression.
This two step proces is neccesarry as postfix notation is easy to understand by the computers and infix is easy to understand by humans.

# Examples
```shell
python3.9 calculator.py "(20 * (30 + 10) / (10 * 2))"

POSTFIX EXPRESSION: 20 30 10 + * 10 2 * /
RESULT: 40.0

python3.9 calculator.py "(20 * (30 % 10) / (10 * 2))"

POSTFIX EXPRESSION: 20 30 10 % * 10 2 * /
RESULT: 0.0

python3.9 calculator.py "(4 + (8 * 3))"
POSTFIX EXPRESSION: 4 8 3 * +
RESULT: 28.0

python3.9 calculator.py "(((7 ^ 2) * (25 + (10 / 5))) - 13)"

POSTFIX EXPRESSION: 7 2 ^ 25 10 5 / + * 13 -
RESULT: 1310.0

python3.9 calculator.py "(((18 / 3) ^ 2) + ((13 + 7) * (5 ^ 2)))"

POSTFIX EXPRESSION: 18 3 / 2 ^ 13 7 + 5 2 ^ * +
RESULT: 536.0
```

# Caveats
Floating numbers cannot be parsed if given in input.