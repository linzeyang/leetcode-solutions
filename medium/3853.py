"""3853. Merge Close Characters"""


class Solution:
    """
    https://leetcode.com/problems/merge-close-characters/
    Biweekly Contest 177
    """

    def mergeCharacters(self, s: str, k: int) -> str:
        lis: list[str] = list(s)

        while True:
            to_merge: int = 0

            for idx, char in enumerate(lis):
                for jdx in range(idx + 1, idx + k + 1):
                    if jdx >= len(lis):
                        break

                    if char == lis[jdx]:
                        to_merge += 1
                        lis.pop(jdx)
                        break

                if to_merge:
                    break

            if not to_merge:
                break

        return "".join(lis)
