"""682. Baseball Game"""

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for oper in operations:
            match oper:
                case "C":
                    scores.pop()
                case "D":
                    scores.append(scores[-1] * 2)
                case "+":
                    scores.append(scores[-1] + scores[-2])
                case _:
                    scores.append(int(oper))

        return sum(scores)
