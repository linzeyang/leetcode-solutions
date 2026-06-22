"""
3963. Create Grid With Exactly One Path

https://leetcode.com/problems/create-grid-with-exactly-one-path/

Biweekly Contest 185
"""


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ["." * n] + ["#" * (n - 1) + "."] * (m - 1)
