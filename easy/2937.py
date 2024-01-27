"""2937. Make Three Strings Equal"""


class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if not (s1[0] == s2[0] == s3[0]):
            return -1

        lenn = min(len(s1), len(s2), len(s3))

        for idx in range(lenn):
            if not (s1[idx] == s2[idx] == s3[idx]):
                return len(s1) + len(s2) + len(s3) - 3 * idx

        return len(s1) + len(s2) + len(s3) - 3 * (idx + 1)
