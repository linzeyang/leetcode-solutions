"""3668. Restore Finishing Order"""

from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_set: set[int] = set(friends)

        return [fri for fri in order if fri in friends_set]
