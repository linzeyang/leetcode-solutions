"""1545. Find Kth Bit in Nth Binary String"""


class Solution:
    """
    https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
    Weekly Contest 201
    """

    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        mid: int = 1 << (n - 1)

        if k == mid:
            return "1"

        elif k < mid:
            return self.findKthBit(n - 1, k)

        return "0" if self.findKthBit(n - 1, 2 * mid - k) == "1" else "1"


if __name__ == "__main__":
    s = Solution()
    assert s.findKthBit(3, 1) == "0"
    assert s.findKthBit(4, 11) == "1"
