"""2325. Decode the Message"""

from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic = {" ": " "}
        count = 0

        for k in key:
            if k == " " or k in dic:
                continue

            dic[k] = ascii_lowercase[count]
            count += 1

        return "".join(dic[char] for char in message)
