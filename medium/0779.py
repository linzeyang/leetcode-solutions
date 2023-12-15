"""779. K-th Symbol in Grammar"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n < 3:
            return k - 1

        prev = self.kthGrammar(n - 1, (k - 1) // 2 + 1)

        if (prev == 0 and k % 2) or (prev == 1 and not k % 2):
            return 0

        return 1
