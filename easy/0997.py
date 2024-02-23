"""997. Find the Town Judge"""

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1

        trusting_count = {}
        trusted_count = {}

        for person_a, person_b in trust:
            if person_a not in trusting_count:
                trusting_count[person_a] = 1
            else:
                trusting_count[person_a] += 1

            if person_b not in trusted_count:
                trusted_count[person_b] = 1
            else:
                trusted_count[person_b] += 1

        candidates = []

        for person, count in trusted_count.items():
            if count == n - 1 and person not in trusting_count:
                candidates.append(person)

        if len(candidates) != 1:
            return -1

        return candidates[0]
