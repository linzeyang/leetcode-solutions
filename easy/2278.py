"""2278. Percentage of Letter in String"""


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int(s.count(letter) / len(s) * 100)
