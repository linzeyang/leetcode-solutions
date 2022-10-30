"""1704. Determine if String Halves Are Alike"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        target = {"a", "e", "i", "o", "u"}
        half = len(s) // 2
        s = s.lower()
        count_a = count_b = 0

        for i in range(half):
            if s[i] in target:
                count_a += 1
            if s[half + i] in target:
                count_b += 1

        return count_a == count_b
