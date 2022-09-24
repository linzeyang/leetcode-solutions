"""
49. Group Anagrams
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Very slow:
        # Runtime: 265 ms, faster than 11.94% of Python3 online submissions for Group Anagrams.
        # Memory Usage: 18 MB, less than 54.01% of Python3 online submissions for Group Anagrams.
        mapping = {}

        for word in strs:
            re = tuple(sorted(word))

            if re not in mapping:
                mapping[re] = [word]

            else:
                mapping[re].append(word)

        return list(mapping.values())
