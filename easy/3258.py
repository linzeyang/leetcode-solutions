"""3258. Count Substrings That Satisfy K-Constraint I"""


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        out = 0

        for idx in range(len(s)):
            num_0 = num_1 = 0

            for jdx in range(idx, len(s)):
                if s[jdx] == "0":
                    num_0 += 1
                else:
                    num_1 += 1

                if num_0 > k and num_1 > k:
                    break

                out += 1

        return out
