"""451. Sort Characters By Frequency"""

import heapq
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq: dict[str, int] = {}

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        queue: list[tuple[int, str]] = []

        for char, fre in freq.items():
            heapq.heappush(queue, (-fre, char))

        out: list[str] = []

        for _ in range(len(freq)):
            neg_fre, char = heapq.heappop(queue)
            out.append(char * -neg_fre)

        return "".join(out)


class Solution2:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        return "".join(
            char * count
            for char, count in sorted(
                counter.items(), key=lambda item: item[1], reverse=True
            )
        )
