"""3847. Find the Score Difference in a Game"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/find-the-score-difference-in-a-game/
    Weekly Contest 490
    """

    def scoreDifference(self, nums: List[int]) -> int:
        score1 = score2 = 0

        player_1_active: bool = True

        for idx, num in enumerate(nums):
            if num & 1:
                player_1_active = not player_1_active

            if idx % 6 == 5:
                player_1_active = not player_1_active

            if player_1_active:
                score1 += num
            else:
                score2 += num

        return score1 - score2
