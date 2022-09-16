"""
258. Add Digits
"""


class Solution:
    def addDigits(self, num: int) -> int:
        # Very slow:
        # Runtime: 79 ms, faster than 5.08% of Python3 online submissions for Add Digits.
        # Memory Usage: 13.9 MB, less than 9.15% of Python3 online submissions for Add Digits.
        while True:
            num = sum(map(int, str(num)))
            if num < 10:
                return num
