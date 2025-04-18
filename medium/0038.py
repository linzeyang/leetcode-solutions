"""38. Count and Say"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        return self._rle(self.countAndSay(n - 1))

    def _rle(self, string: str) -> str:
        out: list[str] = []

        char = string[0]
        count = 1

        for idx in range(1, len(string)):
            if string[idx] == char:
                count += 1
            else:
                out.append(f"{count}{char}")
                char = string[idx]
                count = 1

        out.append(f"{count}{char}")

        return "".join(out)
