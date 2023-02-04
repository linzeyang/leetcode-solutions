"""824. Goat Latin"""


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        out = []

        for idx, word in enumerate(sentence.split()):
            match word[0].lower():
                case "a" | "e" | "i" | "o" | "u":
                    out.append(f"{word}ma{'a' * (idx + 1)}")
                case _:
                    out.append(f"{word[1:]}{word[0]}ma{'a' * (idx + 1)}")

        return " ".join(out)
