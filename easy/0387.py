"""387. First Unique Character in a String"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapping: dict[str, list[int]] = {}

        for idx, char in enumerate(s):
            if char not in mapping:
                mapping[char] = [1, idx]
            else:
                mapping[char][0] += 1

        for count, idx in mapping.values():
            if count == 1:
                return idx

        return -1
