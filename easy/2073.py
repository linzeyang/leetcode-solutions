"""2073. Time Needed to Buy Tickets"""

from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        out = 0
        finished = False

        while True:
            for idx, tic in enumerate(tickets):
                if idx == k:
                    out += 1
                    if tic == 1:
                        finished = True
                        break

                    tickets[idx] = tic - 1

                elif tic > 0:
                    out += 1
                    tickets[idx] = tic - 1

            if finished:
                break

        return out
