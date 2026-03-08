"""1758. Minimum Changes To Make Alternating Binary String"""


class Solution:
    """
    https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
    Weekly Contest 228
    """

    def minOperations(self, s: str) -> int:
        # Count operations needed to make s alternating starting with '0' ("0101...")
        ops = 0

        for i, char in enumerate(s):
            # Check if char matches the expected pattern:
            # 0 at even indices, 1 at odd indices
            if int(char) != (i & 1):
                ops += 1

        # Operations for starting with '1' is len(s) - ops
        return min(ops, len(s) - ops)
