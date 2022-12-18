"""1624. Largest Substring Between Two Equal Characters"""


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        temp = {}

        for idx, char in enumerate(s):
            if char not in temp:
                temp[char] = [idx, None]
            else:
                temp[char][1] = idx

        out = max(temp.values(), key=lambda lis: (lis[1] or -1) - lis[0])

        if out[1] is None:
            return -1

        return out[1] - out[0] - 1
