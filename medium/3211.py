"""3211. Generate Binary Strings Without Adjacent Zeros"""

from typing import List


class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]

        out: list[str] = []

        for part in self.validStrings(n - 1):
            if part.endswith("1"):
                out.append(part + "0")

            out.append(part + "1")

        return out
