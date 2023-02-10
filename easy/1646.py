"""1646. Get Maximum in Generated Array"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        temp = [0, 1]

        for idx in range(2, n + 1):
            if idx % 2 == 0:
                temp.append(temp[idx // 2])
            else:
                temp.append(temp[(idx - 1) // 2] + temp[(idx - 1) // 2 + 1])

        return max(temp)
