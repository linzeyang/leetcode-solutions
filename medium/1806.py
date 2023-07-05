"""1806. Minimum Number of Operations to Reinitialize a Permutation"""


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        lis = list(range(n))
        new = lis[:]

        count = 0

        while True:
            new = [
                new[i // 2] if i % 2 == 0 else new[n // 2 + (i - 1) // 2]
                for i in range(n)
            ]
            count += 1

            if new[1] == 1:
                break

        return count
