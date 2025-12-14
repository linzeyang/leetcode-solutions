"""3776. Minimum Moves to Balance Circular Array"""

from typing import List


class Solution:
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance) < 0:
            return -1

        target_idx: int = -1

        for idx, num in enumerate(balance):
            if num < 0:
                target_idx = idx
                break
        else:
            return 0

        out: int = 0

        for offset in range(1, len(balance) // 2 + 1):
            left_idx: int = (target_idx - offset) % len(balance)
            right_idx: int = (target_idx + offset) % len(balance)

            to_transfer: int = min(balance[left_idx], abs(balance[target_idx]))

            balance[left_idx] -= to_transfer
            balance[target_idx] += to_transfer

            out += offset * to_transfer

            if balance[target_idx] >= 0:
                break

            to_transfer: int = min(balance[right_idx], abs(balance[target_idx]))

            balance[right_idx] -= to_transfer
            balance[target_idx] += to_transfer

            out += offset * to_transfer

            if balance[target_idx] >= 0:
                break

        return out
