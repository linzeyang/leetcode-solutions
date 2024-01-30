"""150. Evaluate Reverse Polish Notation"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list[int] = []

        for token in tokens:
            match token:
                case "+":
                    val = stack.pop() + stack.pop()
                case "-":
                    val = -(stack.pop() - stack.pop())
                case "*":
                    val = stack.pop() * stack.pop()
                case "/":
                    a, b = stack.pop(), stack.pop()
                    val = int(b / a)
                case _:
                    val = int(token)

            stack.append(val)

        return stack[-1]
