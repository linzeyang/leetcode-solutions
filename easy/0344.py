"""344. Reverse String"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for idx in range(len(s) // 2):
            s[idx], s[-idx - 1] = s[-idx - 1], s[idx]
