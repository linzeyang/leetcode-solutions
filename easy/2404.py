"""2404. Most Frequent Even Element"""

from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        maxx = 0

        temp = {}

        for num in nums:
            if num % 2:
                continue

            if num not in temp:
                freq = 1
                temp[num] = freq
            else:
                freq = temp[num] + 1
                temp[num] = freq

            if freq > maxx:
                maxx = freq

        return min((num for num, count in temp.items() if count == maxx), default=-1)
