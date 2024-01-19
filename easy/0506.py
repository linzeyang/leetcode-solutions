"""506. Relative Ranks"""

from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = dict(
            zip(sorted(score, reverse=True), range(1, len(score) + 1), strict=False)
        )

        out = []

        for s in score:
            if dic[s] == 1:
                out.append("Gold Medal")
            elif dic[s] == 2:
                out.append("Silver Medal")
            elif dic[s] == 3:
                out.append("Bronze Medal")
            else:
                out.append(str(dic[s]))

        return out
