"""1299. Replace Elements with Greatest Element on Right Side"""


from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if (length := len(arr)) == 1:
            return [-1]

        res = arr[-1]

        for i in range(2, length):
            ori = arr[-i]
            arr[-i] = res
            res = max(res, ori)

        arr[-1] = -1
        arr[0] = res

        return arr
