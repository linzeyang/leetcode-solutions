"""2138. Divide a String Into Groups of Size k"""

from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        out = [s[idx: idx + k] for idx in range(0, len(s), k)]

        if (last_len := len(out[-1])) < k:
            out[-1] = f"{out[-1]}{fill * (k - last_len)}"

        return out
