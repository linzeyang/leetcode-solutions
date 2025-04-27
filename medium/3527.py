"""3527. Find the Most Common Response"""

from collections import Counter
from typing import List


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        unique_resp_list: list[str] = []

        for response in responses:
            unique_resp_list.extend(list(set(response)))

        counter = Counter(unique_resp_list)

        max_freq = max(counter.values())

        return sorted(key for key, val in counter.items() if val == max_freq)[0]
