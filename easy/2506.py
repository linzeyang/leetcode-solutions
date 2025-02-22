"""2506. Count Pairs Of Similar Strings"""

from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        mapping: dict[tuple[str, ...], list[int]] = {}

        for idx, word in enumerate(words):
            char_set = tuple(sorted(set(word)))

            if char_set not in mapping:
                mapping[char_set] = [idx]
            else:
                mapping[char_set].append(idx)

        out = 0

        for idxs in mapping.values():
            if (length := len(idxs)) < 2:
                continue

            out += (length - 1) * length // 2

        return out
