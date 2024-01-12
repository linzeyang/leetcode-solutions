"""1491. Average Salary Excluding the Minimum and Maximum Salary"""

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:-1]) / (len(salary) - 2)


class Solution2:
    def average(self, salary: List[int]) -> float:
        minn = maxx = salary[0]
        summ = 0

        for sal in salary:
            summ += sal

            if sal < minn:
                minn = sal
            elif sal > maxx:
                maxx = sal

        return (summ - minn - maxx) / (len(salary) - 2)
