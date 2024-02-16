"""1481. Least Number of Unique Integers after K Removals"""

from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = {}

        for num in arr:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        counts = sorted(counter.values(), reverse=True)

        while counts:
            if counts[-1] > k:
                break
            elif counts[-1] == k:
                counts.pop()
                break
            else:
                k -= counts[-1]
                counts.pop()

        return len(counts)
