"""3760. Maximum Substrings With Distinct Start"""


class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))
