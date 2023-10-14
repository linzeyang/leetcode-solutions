"""2895. Minimum Processing Time"""

from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort(reverse=False)

        return max(
            processorTime[idx] + tasks[idx * 4 + 3] for idx in range(len(processorTime))
        )
