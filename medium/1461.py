"""1461. Check If a String Contains All Binary Codes of Size K"""


class Solution:
    """
    https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
    Biweekly Contest 27
    """

    def hasAllCodes(self, s: str, k: int) -> bool:
        required: int = 2**k
        possible: int = len(s) - k + 1

        if possible < required:
            return False

        codes: set[str] = set()

        for idx in range(possible):
            codes.add(s[idx : idx + k])

            if len(codes) == required:
                return True

        return False
