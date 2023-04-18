"""2643. Row With Maximum Ones"""

from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxx = maxx_row = 0

        for idx, lis in enumerate(mat):
            num_of_ones = lis.count(1)

            if num_of_ones > maxx:
                maxx = num_of_ones
                maxx_row = idx

        return [maxx_row, maxx]
