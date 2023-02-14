"""1869. Longer Contiguous Segments of Ones than Zeros"""


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        if len(s) == 1:
            return s[0] == "1"

        zero_streak = one_streak = 0
        current = s[0]
        current_streak = 1

        for idx in range(1, len(s)):
            if s[idx] == current:
                current_streak += 1
            else:
                if current == "0":
                    if current_streak > zero_streak:
                        zero_streak = current_streak
                else:
                    if current_streak > one_streak:
                        one_streak = current_streak

                current = s[idx]
                current_streak = 1

        if current == "0":
            if current_streak > zero_streak:
                zero_streak = current_streak
        else:
            if current_streak > one_streak:
                one_streak = current_streak

        return one_streak > zero_streak
