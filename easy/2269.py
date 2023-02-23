"""2269. Find the K-Beauty of a Number"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        out = 0
        str_num = str(num)

        for idx in range(len(str_num) - k + 1):
            if (sub := int(str_num[idx: idx + k])) != 0 and num % sub == 0:
                out += 1

        return out
