"""2011. Final Value of Variable After Performing Operations"""

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        out = 0

        for oper in operations:
            if "--" in oper:
                out -= 1
            else:
                out += 1

        return out
