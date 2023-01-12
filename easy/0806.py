"""806. Number of Lines To Write String"""

from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        num_of_lines = 1
        line_width = 0

        for char in s:
            width = widths[ord(char) - ord("a")]

            if line_width + width <= 100:
                line_width += width
            else:
                num_of_lines += 1
                line_width = width

        return [num_of_lines, line_width]
