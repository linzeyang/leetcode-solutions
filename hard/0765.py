"""765. Couples Holding Hands"""

from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        count = 0

        for idx in range(0, len(row), 2):
            person1, person2 = row[idx], row[idx + 1]

            desired_person2 = (person1 - 1) if person1 & 1 else (person1 + 1)

            if person2 == desired_person2:
                continue

            desired_idx = row.index(desired_person2)
            row[idx + 1], row[desired_idx] = row[desired_idx], row[idx + 1]
            count += 1

        return count
