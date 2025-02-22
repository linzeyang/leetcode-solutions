"""1415. The k-th Lexicographical String of All Happy Strings of Length n"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        num_of_possibilities = 3 * 2 ** (n - 1)

        if k > num_of_possibilities:
            return ""

        len_sec = 2 ** (n - 1)

        div, mod = divmod(k - 1, len_sec)

        out: list[str] = []

        prev = ""

        while len(out) < n:
            if not out:
                char = "abc"[div]
            elif prev == "a":
                char = "bc"[div]
            elif prev == "b":
                char = "ac"[div]
            else:
                char = "ab"[div]

            out.append(char)

            prev = char

            len_sec //= 2

            if len_sec:
                div, mod = divmod(mod, len_sec)

        return "".join(out)
