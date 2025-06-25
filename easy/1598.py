"""1598. Crawler Log Folder"""

from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth: int = 0

        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                depth = max(0, depth - 1)
            else:
                depth += 1

        return depth
