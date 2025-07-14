"""2410. Maximum Matching of Players With Trainers"""

from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        i = j = count = 0

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                # Match found
                count += 1
                i += 1
                j += 1
            else:
                # Skip current trainer (it's too weak), check next stronger trainer
                j += 1

        return count
