"""717. 1-bit and 2-bit Characters"""

from collections import deque
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        length: int = len(bits)

        if length == 1:
            return bits[0] == 0

        que: deque[int] = deque(bits)

        while len(que) > 1:
            if que[0] == 1:
                que.popleft()
                que.popleft()
            else:
                que.popleft()

        return bool(que and que[0] == 0)
