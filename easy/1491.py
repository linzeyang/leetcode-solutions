"""1491. Average Salary Excluding the Minimum and Maximum Salary"""

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:-1]) / (len(salary) - 2)
