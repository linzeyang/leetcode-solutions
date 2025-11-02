"""3289. The Two Sneaky Numbers of Digitville"""

from typing import List


class Solution2:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        """Optimal solution: Clean set approach with early termination"""

        seen: set[int] = set()
        out: list[int] = []

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                out.append(num)

                if len(out) == 2:  # Early termination - we know there are exactly 2
                    break

        return out
