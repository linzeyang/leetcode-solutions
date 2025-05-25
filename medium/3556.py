"""3556. Sum of Largest Prime Substrings"""


class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        candidates: set[int] = set()

        for idx in range(len(s)):
            for jdx in range(idx, len(s)):
                candidates.add(int(s[idx : jdx + 1]))

        out: set[int] = set()

        for candidate in candidates:
            if self._is_prime(candidate):
                out.add(candidate)

        if not out:
            return 0

        return sum(sorted(out, reverse=True)[:3])

    def _is_prime(self, num: int) -> bool:
        if num < 2:
            return False

        if num in (2, 3, 5, 7, 11, 13, 17, 19):
            return True

        if num & 1 == 0:
            return False

        for factor in range(3, int(num**0.5) + 1, 2):
            if num % factor == 0:
                return False

        return True
