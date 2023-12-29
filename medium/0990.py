"""990. Satisfiability of Equality Equations"""

from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        temp: dict[str, str] = {}

        for equation in equations:
            oper = equation[1:3]

            if oper != "==":
                continue

            left, right = equation[0], equation[3]

            if left not in temp:
                temp[left] = left

            if right not in temp:
                temp[right] = left

            left_ancestor = self._find_ancestor(left, temp)
            right_ancestor = self._find_ancestor(right, temp)

            if left_ancestor != right_ancestor:
                temp[right_ancestor] = left_ancestor

        for equation in equations:
            oper = equation[1:3]

            if oper == "==":
                continue

            left, right = equation[0], equation[3]

            if left not in temp:
                temp[left] = left

            if right not in temp:
                temp[right] = right

            if self._find_ancestor(left, temp) == self._find_ancestor(right, temp):
                return False

        return True

    def _find_ancestor(self, member: str, relations: dict[str, str]) -> str:
        while (ancestor := relations[member]) != member:
            member = ancestor

        return member
