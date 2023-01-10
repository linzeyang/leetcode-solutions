"""821. Shortest Distance to a Character"""

from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        iter_idxes = (idx for idx, char in enumerate(s) if char == c)
        prev_idx = -1
        curr_idx = next(iter_idxes)

        out = []

        for i in range(len(s)):
            if i == curr_idx:
                out.append(0)
                prev_idx = i

                try:
                    curr_idx = next(iter_idxes)
                except StopIteration:
                    curr_idx = -1
            elif i < curr_idx:
                if prev_idx == -1:
                    out.append(curr_idx - i)
                else:
                    out.append(min(i - prev_idx, curr_idx - i))
            elif curr_idx == -1:
                out.append(i - prev_idx)

        return out
