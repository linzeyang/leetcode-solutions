"""3823. Reverse Letters Then Special Characters in a String"""


class Solution:
    """
    https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/
    Biweekly Contest 175
    """

    def reverseByType(self, s: str) -> str:
        letter_idxs: list[int] = []
        punc_idxs: list[int] = []

        for idx, char in enumerate(s):
            if char.isalpha():
                letter_idxs.append(idx)
            else:
                punc_idxs.append(idx)

        temp: list[str] = [""] * len(s)

        for jdx, kdx in zip(letter_idxs, reversed(letter_idxs), strict=True):
            temp[jdx] = s[kdx]

        for jdx, kdx in zip(punc_idxs, reversed(punc_idxs), strict=True):
            temp[jdx] = s[kdx]

        return "".join(temp)
