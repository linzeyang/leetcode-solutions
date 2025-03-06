"""1328. Break a Palindrome"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        palin_list: list[str] = list(palindrome)

        length = len(palin_list)

        if palin_list[0] != "a":
            palin_list[0] = "a"
        elif length & 1:
            mid = length // 2

            for idx in range(1, length):
                if idx == mid:
                    continue

                if palin_list[idx] != "a":
                    palin_list[idx] = "a"
                    break
            else:
                palin_list[-1] = "b"
        else:
            for idx in range(1, length):
                if palin_list[idx] != "a":
                    palin_list[idx] = "a"
                    break
            else:
                palin_list[-1] = "b"

        return "".join(palin_list)
