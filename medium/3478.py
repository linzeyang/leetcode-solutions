"""3478. Choose K Elements With Maximum Sum"""

import heapq
from typing import List


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        length = len(nums1)

        out: list[int] = [0] * length

        new_nums1 = [(idx, num) for idx, num in enumerate(nums1)]
        new_nums1.sort(key=lambda tup: tup[1])

        candidates: list[int] = []
        heapq.heapify(candidates)

        summ = 0

        for jdx in range(1, length):
            idx, num = new_nums1[jdx]

            if len(candidates) >= k:
                popped = heapq.heappushpop(candidates, nums2[new_nums1[jdx - 1][0]])

                summ += nums2[new_nums1[jdx - 1][0]] - popped
            else:
                heapq.heappush(candidates, nums2[new_nums1[jdx - 1][0]])

                summ += nums2[new_nums1[jdx - 1][0]]

            if num == new_nums1[jdx - 1][1]:
                out[idx] = out[new_nums1[jdx - 1][0]]
            else:
                out[idx] = summ

        return out


if __name__ == "__main__":
    testcases: list[tuple] = [
        ([[4, 2, 1, 5, 3], [10, 20, 30, 40, 50], 2], [80, 30, 0, 80, 50]),
        ([[2, 2, 2, 2], [3, 1, 2, 3], 1], [0, 0, 0, 0]),
        (
            [[18, 11, 24, 9, 10, 11, 7, 29, 16], [28, 26, 27, 4, 2, 19, 23, 1, 2], 1],
            [26, 23, 28, 23, 23, 23, 0, 28, 26],
        ),
    ]

    for tup in testcases:
        assert Solution().findMaxSum(*tup[0]) == tup[1]
