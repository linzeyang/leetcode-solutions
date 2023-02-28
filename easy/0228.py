"""228. Summary Ranges"""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if (length := len(nums)) == 0:
            return []

        if length == 1:
            return [str(nums[0])]

        temp = [nums[0]]
        out = []

        for idx in range(1, length):
            if nums[idx] - 1 == nums[idx - 1]:
                temp.append(nums[idx])
            else:
                if len(temp) == 1:
                    out.append(str(temp[0]))
                else:
                    out.append(f"{temp[0]}->{temp[-1]}")
                temp = [nums[idx]]

        if len(temp) == 1:
            out.append(str(temp[0]))
        else:
            out.append(f"{temp[0]}->{temp[-1]}")
            temp = [nums[idx]]

        return out
