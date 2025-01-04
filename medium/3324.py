"""3324. Find the Sequence of Strings Appeared on the Screen"""

from string import ascii_lowercase
from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        out: list[str] = []

        for char in target:
            if not out:
                last = ""
            else:
                last = out[-1]

            for letter in ascii_lowercase:
                out.append(last + letter)

                if letter == char:
                    break

        return out
