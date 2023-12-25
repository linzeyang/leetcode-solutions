"""201. Bitwise AND of Numbers Range"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left

        count = 0

        while left != right:
            left >>= 1
            right >>= 1
            count += 1

        return left << count
