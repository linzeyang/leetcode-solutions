"""
4043. Count Rotations With Exactly K Equal Adjacent Pairs

https://leetcode.com/problems/count-rotations-with-exactly-k-equal-adjacent-pairs/

Weekly Contest 518
"""


class Solution:
    def countRotations(self, s: str, k: int) -> int:
        equals: list[int] = []

        for idx in range(len(s)):
            equals.append(int(s[idx] == s[(idx + 1) % len(s)]))

        score: int = sum(equals[:-1])

        out: int = int(score == k)

        for idx in range(len(equals) - 1):
            score = score - equals[idx] + equals[idx - 1]

            if score == k:
                out += 1

        return out
