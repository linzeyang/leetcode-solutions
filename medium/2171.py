"""2171. Removing Minimum Number of Magic Beans"""

from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        summ = beans_to_keep = 0

        for idx, num in enumerate(beans):
            summ += num
            sub = (len(beans) - idx) * num

            if sub > beans_to_keep:
                beans_to_keep = sub

        return summ - beans_to_keep
