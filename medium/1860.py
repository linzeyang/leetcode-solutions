"""1860. Incremental Memory Leak"""

from typing import List


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        sec = 1

        while memory1 >= sec or memory2 >= sec:
            if memory1 >= memory2:
                memory1 -= sec
            else:
                memory2 -= sec
            sec += 1

        return [sec, memory1, memory2]
