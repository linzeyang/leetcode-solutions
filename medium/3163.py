"""3163. String Compression III"""


class Solution:
    def compressedString(self, word: str) -> str:
        if len(word) == 1:
            return "1" + word

        out: list[str] = []

        count = 1
        char = word[0]

        for idx in range(1, len(word)):
            if word[idx] != char or count >= 9:
                out.append(str(count) + char)
                count = 1
                char = word[idx]
            else:
                count += 1

        out.append(str(count) + char)

        return "".join(out)
