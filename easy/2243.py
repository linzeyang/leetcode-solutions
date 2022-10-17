"""2243. Calculate Digit Sum of a String"""


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = _do_one_round(s, k)

        return s


def _do_one_round(ss, k):
    out = []

    i = 0

    while seg := ss[i * k: (i + 1) * k]:
        out.append(sum(int(n) for n in seg))
        i += 1

    return "".join(str(n) for n in out)
