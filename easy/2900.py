"""2900. Longest Unequal Adjacent Groups Subsequence I"""

from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        target_zero = 0
        idx_zero: list[int] = []

        target_one = 1
        idx_one: list[int] = []

        for idx, group in enumerate(groups):
            if group == target_zero:
                target_zero = int(not target_zero)
                idx_zero.append(idx)
            if group == target_one:
                target_one = int(not target_one)
                idx_one.append(idx)

        idxs = idx_zero if len(idx_zero) > len(idx_one) else idx_one

        return [words[idx] for idx in idxs]


if __name__ == "__main__":
    testcases: tuple[tuple[tuple[list[str], list[int]], list[str]], ...] = (
        ((["e", "a", "b"], [0, 0, 1]), ["e", "b"]),
        ((["a", "b", "c", "d"], [1, 0, 1, 1]), ["a", "b", "c"]),
        ((["d", "e", "f"], [1, 1, 1]), ["d"]),
        ((["tu", "rv", "bn"], [0, 0, 0]), ["tu"]),
        ((["c", "f", "y", "i"], [1, 0, 1, 1]), ["c", "f", "y"]),
        ((["c"], [0]), ["c"]),
        ((["d"], [1]), ["d"]),
    )

    for case in testcases:
        assert Solution().getLongestSubsequence(*case[0]) == case[1]
