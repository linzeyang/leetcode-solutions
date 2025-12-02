"""3761. Minimum Absolute Distance Between Mirror Pairs"""

from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # Stores { reverse(nums[i]) : i }
        # We store the index 'i' for the reversed value of nums[i]
        # to check against future nums[j].
        seen_rev: dict[int, int] = {}
        out: float = float("inf")

        for jdx, num in enumerate(nums):
            # Check if current num matches a previously seen reverse(nums[i])
            # The condition is reverse(nums[i]) == nums[j]
            if num in seen_rev:
                distance: int = jdx - seen_rev[num]
                # 1 is the smallest possible distance, so we can return early
                if distance == 1:
                    return 1
                out = min(out, distance)

            # Update the map with the reverse of the current number.
            # We overwrite with the current index 'j' because if we find a match later,
            # using a larger index 'i' will result in a smaller distance (j' - i).
            seen_rev[self._reverse(num)] = jdx

        return out if out != float("inf") else -1

    def _reverse(self, num: int) -> int:
        return int(str(num)[::-1])
