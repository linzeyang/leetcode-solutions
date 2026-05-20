"""
3931. Check Adjacent Digit Differences

https://leetcode.com/problems/check-adjacent-digit-differences/

Weekly Contest 502
"""


class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for idx in range(len(s) - 1):
            if abs(ord(s[idx]) - ord(s[idx + 1])) > 2:
                return False

        return True
