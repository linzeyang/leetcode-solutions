"""1784. Check if Binary String Has at Most One Segment of Ones"""


class Solution:
    """
    https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
    Weekly Contest 231
    """

    def checkOnesSegment(self, s: str) -> bool:
        return "0" not in s.strip("0")
