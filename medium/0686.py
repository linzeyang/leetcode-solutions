"""686. Repeated String Match"""


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Very slow!
        for idx, char in enumerate(a):
            if char != b[0]:
                continue

            repeat = 1
            jdx = idx

            for ch in b:
                if jdx == len(a):
                    jdx = 0
                    repeat += 1

                if a[jdx] != ch:
                    break

                jdx += 1
            else:
                return repeat

        return -1
