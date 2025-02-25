"""3461. Check If Digits Are Equal in String After Operations I"""


# most straight-forward way, O(N ** 2) time-complexity,
# suitable when s is short enough
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        lis: list[int] = [int(char) for char in s]

        while len(lis) > 2:
            temp: list[int] = []

            for idx in range(len(lis) - 1):
                temp.append((lis[idx] + lis[idx + 1]) % 10)

            lis = temp

        return lis[0] == lis[1]


# more universal way, O(N) time-complexity
class Solution2:
    def hasSameDigits(self, s: str) -> bool:
        lis: list = [int(char) for char in s]

        length = len(lis)

        level = length - 2

        factors: list[int] = [1]

        for k in range(level // 2):
            factors.append(factors[-1] * (level - k) // (k + 1))

        if level & 1:
            factors += factors[::-1]
        else:
            factors += factors[-2::-1]

        left = sum(a * b for a, b in zip(factors, lis[: length - 1], strict=True))

        right = sum(a * b for a, b in zip(factors, lis[1:length], strict=True))

        return left % 10 == right % 10
