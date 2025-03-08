"""3386. Button with Longest Push Time"""

from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        min_idx, max_time = events[0]

        for idx in range(1, len(events)):
            button_idx, timestamp = events[idx]

            time = timestamp - events[idx - 1][1]

            if time > max_time:
                max_time = time
                min_idx = button_idx
            elif time == max_time and button_idx < min_idx:
                min_idx = button_idx

        return min_idx
