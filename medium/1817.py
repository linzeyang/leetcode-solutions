"""1817. Finding the Users Active Minutes"""

from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        out = [0] * k

        temp: dict[int, set[int]] = {}

        for user, minute in logs:
            if user not in temp:
                temp[user] = set({minute})
            else:
                temp[user].add(minute)

        for mset in temp.values():
            out[len(mset) - 1] += 1

        return out
