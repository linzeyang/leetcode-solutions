"""2133. Check if Every Row and Column Contains All Numbers"""

from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        length = len(matrix)
        col_mapping = {}

        for row in range(length):
            row_set = set(matrix[row])

            if len(row_set) < length:
                return False

            for col in range(length):
                if col not in col_mapping:
                    col_mapping[col] = {matrix[row][col]}
                elif matrix[row][col] not in col_mapping[col]:
                    col_mapping[col].add(matrix[row][col])
                else:
                    return False

        return True
