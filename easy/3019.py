"""3019. Number of Changing Keys"""


class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        return sum(1 for idx in range(1, len(s)) if s[idx] != s[idx - 1])
