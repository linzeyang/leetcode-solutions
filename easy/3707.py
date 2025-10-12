"""3707. Equal Score Substrings"""


class Solution:
    def scoreBalance(self, s: str) -> bool:
        pre_sums: set[int] = set()
        pre_sum: int = 0

        for char in s:
            pre_sum += ord(char) - ord("a") + 1
            pre_sums.add(pre_sum)

        return pre_sum & 1 == 0 and (pre_sum // 2) in pre_sums
