"""1365. How Many Numbers Are Smaller Than the Current Number"""

from collections import Counter
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cc = Counter(nums)

        return [sum(v for k, v in cc.items() if k < num) for num in nums]
