"""
6. Zigzag Conversion
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        matrix = [[] for _ in range(numRows)]
        seg = 2 * numRows - 2

        for i in range(len(s)):
            remain = i % seg

            if remain < numRows:
                matrix[remain].append(s[i])
            else:
                matrix[numRows - remain - 2].append(s[i])

        return "".join("".join(c for c in line) for line in matrix)
