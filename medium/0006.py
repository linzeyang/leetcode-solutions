"""
6. Zigzag Conversion
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        matrix = [[] for _ in range(numRows)]
        seg = 2 * numRows - 2

        for idx, char in enumerate(s):
            remain = idx % seg

            if remain < numRows:
                matrix[remain].append(char)
            else:
                matrix[numRows - remain - 2].append(char)

        return "".join("".join(line) for line in matrix)
