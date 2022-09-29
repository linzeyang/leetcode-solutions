"""557. Reverse Words in a String III"""


class Solution:
    def reverseWords(self, s: str) -> str:
        # Runtime: 72 ms, faster than 45.99% of Python3 online submissions for Reverse Words in a String III.
        # Memory Usage: 14.8 MB, less than 13.00% of Python3 online submissions for Reverse Words in a String III.
        return " ".join(word[::-1] for word in s.split())
