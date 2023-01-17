"""944. Delete Columns to Make Sorted"""

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num_of_columns = len(strs[0])
        count = 0

        for idx in range(num_of_columns):
            chars = [string[idx] for string in strs]

            if chars != sorted(chars):
                count += 1

        return count
