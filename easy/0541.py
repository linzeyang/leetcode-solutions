"""541. Reverse String II"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        parts: list[str] = []

        for idx in range(0, len(s), k):
            parts.append(s[idx : idx + k])

        for jdx in range(0, len(parts), 2):
            parts[jdx] = parts[jdx][::-1]

        return "".join(parts)
