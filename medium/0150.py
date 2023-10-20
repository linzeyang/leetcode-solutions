"""150. Evaluate Reverse Polish Notation"""

from operator import add, mul, sub, truediv
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mapping = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda num1, num2: int(truediv(num1, num2)),
        }

        stack: list[int] = []

        for token in tokens:
            if token not in mapping:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                res = mapping[token](num2, num1)
                stack.append(res)

        return stack[0]
