"""49. Group Anagrams"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {}

        for word in strs:
            re = tuple(sorted(word))

            if re not in mapping:
                mapping[re] = [word]

            else:
                mapping[re].append(word)

        return list(mapping.values())
