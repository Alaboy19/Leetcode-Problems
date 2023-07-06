'''
150. Evaluate Reverse Polish Notation
Given:
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:

The valid operators are '+', '-', '*', and '/'
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
'''

def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        current_results = []
        for token in tokens:
            if token not in operators:
                current_results.append(int(token))
            else:
                b, a = current_results.pop(), current_results.pop()
                if token == '+':
                    current_results.append(a + b)
                elif token == '-':
                    current_results.append(a - b)
                elif token == '*':
                    current_results.append(a * b)
                else:
                    current_results.append(int(a / b))
        return current_results[0]
