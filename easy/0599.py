"""599. Minimum Index Sum of Two Lists"""

from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        phrase_to_index_sum: dict[str, int] = {}

        phrase_to_jdx: dict[str, int] = {
            phrase: jdx for jdx, phrase in enumerate(list2)
        }

        for idx, phrase in enumerate(list1):
            if phrase not in phrase_to_jdx:
                continue

            phrase_to_index_sum[phrase] = idx + phrase_to_jdx[phrase]

        min_index_sum: int = min(phrase_to_index_sum.values())

        return [
            phrase
            for phrase in phrase_to_index_sum
            if phrase_to_index_sum[phrase] == min_index_sum
        ]
