"""1854. Maximum Population Year"""

from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        temp = {}

        for log in logs:
            for year in range(log[0], log[1]):
                if year not in temp:
                    temp[year] = 1
                else:
                    temp[year] += 1

        maxx = max(temp.values())

        return min(year for year, count in temp.items() if count == maxx)
