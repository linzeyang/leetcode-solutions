"""1282. Group the People Given the Group Size They Belong To"""

from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        temp: dict[int, list[int]] = {}
        out = []

        for idx, num in enumerate(groupSizes):
            if num not in temp:
                temp[num] = [idx]
            elif len(temp[num]) < num:
                temp[num].append(idx)
            else:
                out.append(temp[num])
                temp[num] = [idx]

        for lis in temp.values():
            out.append(lis)

        return out
