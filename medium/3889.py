"""
3889. Mirror Frequency Distance

https://leetcode.com/problems/mirror-frequency-distance/

Weekly Contest 496
"""

from string import ascii_lowercase, digits

MAPPING: dict[str, str] = dict(
    zip(ascii_lowercase + digits, ascii_lowercase[::-1] + digits[::-1], strict=True)
)


class Solution:
    def mirrorFrequency(self, s: str) -> int:
        counter: dict[str, list[int]] = {}

        for char in s:
            if MAPPING[char] in counter:
                counter[MAPPING[char]][1] += 1
            elif char in counter:
                counter[char][0] += 1
            else:
                counter[char] = [1, 0]

        return sum(abs(v[0] - v[1]) for v in counter.values())
