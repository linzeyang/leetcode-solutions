"""3090. Maximum Length Substring With Two Occurrences"""


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        length = len(s)

        if length < 3:
            return length

        out = 2

        for idx in range(length - 2):
            if length - idx <= out:
                break

            counter = {s[idx]: 1}

            for jdx in range(idx + 1, length):
                if counter.get(s[jdx], 0) < 2:
                    counter[s[jdx]] = counter.get(s[jdx], 0) + 1
                    out = max(out, jdx - idx + 1)
                else:
                    break

        return out
