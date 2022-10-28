"""1773. Count Items Matching a Rule"""

from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        mapping = {
            "type": 0,
            "color": 1,
            "name": 2,
        }

        return len([item for item in items if item[mapping[ruleKey]] == ruleValue])
